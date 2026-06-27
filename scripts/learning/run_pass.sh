#!/usr/bin/env bash
# run_pass.sh START END — run rounds START..END UNATTENDED & RESILIENTLY to finish one pass.
#
# Per round: (idempotent) shard -> run workers until every shard is complete -> run the
# consolidator until its commit lands. On a Codex TOKEN/RATE LIMIT it sleeps WAIT seconds
# (default 1200 = 20 min) and retries — indefinitely for rate limits, with a bounded retry for
# other transient failures. Stops cleanly when the task pool is exhausted.
#
# Resumable: re-running picks up where it left off (skips already-sharded shards and the
# already-committed consolidation; only re-runs incomplete shards).
#
# Env: WAIT (rate-limit sleep, default 1200), TRANSIENT_RETRIES (per phase, default 3),
#      MAX_RATE_WAITS (give up after this many 20-min waits in a row, default 144 = ~48h),
#      PUSH_EACH=1 to git push after each consolidated round, CODEX_MODEL to override model.
set -uo pipefail
START="${1:?usage: run_pass.sh START END}"
END="${2:?usage: run_pass.sh START END}"
WORKERS=5; BATCH=50
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"; cd "$REPO"; mkdir -p logs
WAIT="${WAIT:-1200}"; TRANSIENT_RETRIES="${TRANSIENT_RETRIES:-3}"; MAX_RATE_WAITS="${MAX_RATE_WAITS:-144}"
WORKER_TIMEOUT="${WORKER_TIMEOUT:-3600}"
CODEX=(codex exec --dangerously-bypass-approvals-and-sandbox -C "$REPO" -c shell_environment_policy.inherit=all)
[ -n "${CODEX_MODEL:-}" ] && CODEX+=(-m "$CODEX_MODEL")

ts(){ date +%H:%M:%S; }
log(){ echo "[$(ts)] $*"; }
safe_task(){ printf '%s' "$1" | tr ':/' '__'; }

# Branch-drift guard: a runaway codex once ran `git checkout <other-branch>` and committed a
# round there, orphaning it. Pin the branch we started on and restore it after every codex call.
EXPECT_BRANCH="$(git branch --show-current)"
pin_branch(){
  local b; b="$(git branch --show-current)"
  if [ "$b" != "$EXPECT_BRANCH" ]; then
    log "!! branch drifted to '$b' — restoring '$EXPECT_BRANCH'"
    git checkout "$EXPECT_BRANCH" >/dev/null 2>&1 || true
  fi
}

ratelimited(){  # any of the given log files show a GENUINE rate/usage-limit marker.
  # NB: must NOT match source code. Bare "429" matched "4294967295" (UINT32_MAX) and bare
  # "quota" matched "quotaon" in task source, causing false 20-min sleeps on plain worker
  # crashes. Require actual rate-limit phrasing instead.
  grep -qiE "rate.?limit|too many requests|usage limit|insufficient_quota|quota exceeded|exceeded your current quota|x-ratelimit|retry.?after|429 too many|over.?capacity|overloaded" "$@" 2>/dev/null
}

shard_complete(){  # R k
  local r="$1" k="$2" t safe; local sh="learning/round-$r/shard-$k.txt"
  [ -f "$sh" ] || return 1
  while IFS= read -r t; do t="${t%%#*}"; t="$(printf '%s' "$t"|xargs)"; [ -z "$t" ]&&continue
    safe="$(safe_task "$t")"; [ -f "learning/round-$r/traces/$safe.json" ]||return 1; done < "$sh"
  return 0
}
round_complete(){ local r="$1" k; for k in $(seq 1 $WORKERS); do shard_complete "$r" "$k"||return 1; done; return 0; }
# NB: capture into a var + here-string. `git log | grep -q` under `set -o pipefail` is racy:
# grep -q exits on first match, git log gets SIGPIPE (141), pipefail propagates that as
# failure -> a real match misreads as "not consolidated" and re-runs the consolidator.
consolidated(){ local _l; _l="$(git log --format=%s -100)"; grep -qiE "^consolidate round $1[: ]" <<<"$_l"; }

run_worker(){  # R k
  local r="$1" k="$2"
  { printf 'Use WORKER_ID=%s and ROUND=%s. Solve ONLY learning/round-%s/shard-%s.txt. Do NOT run shard_round.\n\n' "$k" "$r" "$r" "$k"
    cat docs/codex-worker-prompt.md
  } | WORKER_ID="$k" ROUND="$r" timeout "$WORKER_TIMEOUT" "${CODEX[@]}" - > "logs/round-${r}-worker-${k}.log" 2>&1
}

# Returns 0 if the round got fully traced; non-zero if it should be retried (caller decides wait).
worker_wave(){  # R -> runs all incomplete shards once (parallel), then reports completeness
  local r="$1" pids=() k
  for k in $(seq 1 $WORKERS); do
    if ! shard_complete "$r" "$k"; then
      log "  round $r: launching worker $k"; run_worker "$r" "$k" & pids+=($!); sleep 10
    fi
  done
  for p in "${pids[@]:-}"; do [ -n "${p:-}" ] && wait "$p" 2>/dev/null || true; done
  pin_branch
  round_complete "$r"
}

do_round(){
  local R="$1" rate_waits=0 transient=0
  # 1. idempotent shard
  if [ ! -f "learning/round-$R/shard-1.txt" ]; then
    log "round $R: sharding"
    if ! .venv/bin/python scripts/learning/shard_round.py --round "$R" --workers $WORKERS --batch $BATCH; then
      log "round $R: shard_round failed (pool likely EXHAUSTED) — ending pass."; return 9
    fi
  else
    log "round $R: shard exists, resuming"
  fi
  # 2. workers until complete
  while ! round_complete "$R"; do
    worker_wave "$R" && break
    if ratelimited logs/round-${R}-worker-*.log; then
      rate_waits=$((rate_waits+1))
      [ "$rate_waits" -gt "$MAX_RATE_WAITS" ] && { log "round $R: rate-limited $rate_waits× — giving up."; return 1; }
      log "round $R: RATE LIMIT (workers) — sleeping ${WAIT}s (wait #$rate_waits)"; sleep "$WAIT"
    else
      transient=$((transient+1))
      [ "$transient" -gt "$TRANSIENT_RETRIES" ] && { log "round $R: workers failed $transient× (not rate-limit) — giving up."; return 1; }
      log "round $R: incomplete (transient #$transient) — retry in 60s"; sleep 60
    fi
  done
  log "round $R: ROUND COMPLETE — consolidating"
  # 3. consolidator until commit lands
  rate_waits=0; transient=0
  while ! consolidated "$R"; do
    { printf 'Set ROUND=%s. Consolidate round %s now (it is COMPLETE).\n\n' "$R" "$R"; cat docs/codex-consolidator-prompt.md; } \
      | ROUND="$R" timeout "$WORKER_TIMEOUT" "${CODEX[@]}" - > "logs/round-${R}-consolidator.log" 2>&1 || true
    pin_branch
    consolidated "$R" && break
    if ratelimited logs/round-${R}-consolidator.log; then
      rate_waits=$((rate_waits+1))
      [ "$rate_waits" -gt "$MAX_RATE_WAITS" ] && { log "round $R: consolidator rate-limited $rate_waits× — giving up."; return 1; }
      log "round $R: RATE LIMIT (consolidator) — sleeping ${WAIT}s (wait #$rate_waits)"; sleep "$WAIT"
    else
      transient=$((transient+1))
      [ "$transient" -gt "$TRANSIENT_RETRIES" ] && { log "round $R: consolidator failed $transient× — giving up (check log)."; return 1; }
      log "round $R: consolidator did not commit (transient #$transient) — retry in 60s"; sleep 60
    fi
  done
  log "round $R: CONSOLIDATED -> $(git log --oneline -1)"
  [ "${PUSH_EACH:-0}" = "1" ] && { git push 2>&1 | tail -1; }
  # Reclaim disk: the round's traces are committed; runs/ is gitignored per-task scratch
  # (extracted source — ~260MB/task). Left to accumulate it filled a 900G disk (226G) and
  # crashed the pass. The round is done, so clear it before the next round's gen.
  rm -rf runs/* 2>/dev/null || true
  log "round $R: cleared runs/ scratch ($(df -h / | awk 'NR==2{print $4" free"}'))"
  return 0
}

log "===== run_pass $START..$END (WAIT=${WAIT}s, push_each=${PUSH_EACH:-0}) ====="
for ((R=START; R<=END; R++)); do
  log "######## ROUND $R ########"
  do_round "$R"; rc=$?
  if [ "$rc" -eq 9 ]; then log "pool exhausted at round $R — pass complete."; break; fi
  if [ "$rc" -ne 0 ]; then log "round $R FAILED (rc=$rc) — stopping pass."; exit 1; fi
done
log "===== run_pass done ====="
