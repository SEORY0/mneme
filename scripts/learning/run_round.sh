#!/usr/bin/env bash
# run_round.sh R [WORKERS] [BATCH] — fully automate ONE mode-B learning round via headless Codex.
#
#   shard  ->  WORKERS parallel `codex exec` workers (fresh process each)  ->  poll round_status
#          ->  re-run incomplete shards once  ->  serial `codex exec` consolidator
#
# The "intelligence" stays in Codex (gpt-5-codex); mneme only runs gen/verify/submit, so the
# no-LLM-API-inside-mneme rule holds. Each worker is a fresh process => no session-context bloat.
#
# DANGER: uses --dangerously-bypass-approvals-and-sandbox so Codex runs docker/git WITHOUT
# prompting (the consolidator auto-commits). Only run in the authorized/sandboxed benchmark env.
#
# Env overrides: CODEX_MODEL (passed as -m), WORKER_TIMEOUT (s, default 3600),
#                POLL_TRIES (default 60), POLL_SLEEP (s, default 20).
set -uo pipefail

R="${1:?usage: run_round.sh R [WORKERS] [BATCH]}"
WORKERS="${2:-5}"
BATCH="${3:-50}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO"
mkdir -p logs

WORKER_TIMEOUT="${WORKER_TIMEOUT:-3600}"
POLL_TRIES="${POLL_TRIES:-60}"
POLL_SLEEP="${POLL_SLEEP:-20}"
CODEX_MODEL_ARGS=()
[ -n "${CODEX_MODEL:-}" ] && CODEX_MODEL_ARGS=(-m "$CODEX_MODEL")

CODEX=(codex exec --dangerously-bypass-approvals-and-sandbox -C "$REPO"
       -c shell_environment_policy.inherit=all "${CODEX_MODEL_ARGS[@]}")

safe_task() { printf '%s' "$1" | tr ':/' '__'; }

shard_complete() {  # R k -> 0 if every assigned task has a trace
  local r="$1" k="$2" t safe
  local shard="learning/round-$r/shard-$k.txt"
  [ -f "$shard" ] || return 1
  while IFS= read -r t; do
    t="${t%%#*}"; t="$(printf '%s' "$t" | xargs)"; [ -z "$t" ] && continue
    safe="$(safe_task "$t")"
    [ -f "learning/round-$r/traces/$safe.json" ] || return 1
  done < "$shard"
  return 0
}

run_worker() {  # R k
  local r="$1" k="$2"
  { printf 'Use WORKER_ID=%s and ROUND=%s for this run. Solve ONLY learning/round-%s/shard-%s.txt. Do NOT run shard_round.\n\n' "$k" "$r" "$r" "$k"
    cat docs/codex-worker-prompt.md
  } | WORKER_ID="$k" ROUND="$r" timeout "$WORKER_TIMEOUT" "${CODEX[@]}" - \
      > "logs/round-${r}-worker-${k}.log" 2>&1
}

echo "== round $R: shard =="
.venv/bin/python scripts/learning/shard_round.py --round "$R" --workers "$WORKERS" --batch "$BATCH"

run_wave() {  # launch workers for shards passed as args (numbers)
  local pids=() k
  for k in "$@"; do
    echo "  launching worker $k (round $R) -> logs/round-${R}-worker-${k}.log"
    run_worker "$R" "$k" &
    pids+=($!)
    sleep 10   # stagger to spare the submit server
  done
  for p in "${pids[@]}"; do wait "$p" || echo "  worker pid $p exited nonzero (see log)"; done
}

echo "== round $R: worker wave 1 (${WORKERS} parallel) =="
run_wave $(seq 1 "$WORKERS")

# Poll until complete, then re-run any incomplete shards once.
poll_complete() {
  local i
  for ((i=0; i<POLL_TRIES; i++)); do
    bash scripts/learning/round_status.sh "$R" >/dev/null 2>&1 && return 0
    sleep "$POLL_SLEEP"
  done
  return 1
}

if ! poll_complete; then
  echo "== round $R: incomplete after wave 1; re-running incomplete shards =="
  incomplete=()
  for ((k=1; k<=WORKERS; k++)); do shard_complete "$R" "$k" || incomplete+=("$k"); done
  if [ "${#incomplete[@]}" -gt 0 ]; then
    echo "  re-running shards: ${incomplete[*]}"
    run_wave "${incomplete[@]}"
    poll_complete || true
  fi
fi

bash scripts/learning/round_status.sh "$R" || {
  echo "!! round $R still INCOMPLETE — NOT running consolidator (would learn from partial traces)."
  echo "   Inspect logs/round-${R}-worker-*.log, fix, then run the consolidator manually."
  exit 1
}

echo "== round $R: consolidator (serial) -> logs/round-${R}-consolidator.log =="
{ printf 'Set ROUND=%s. Consolidate round %s now (the round is COMPLETE).\n\n' "$R" "$R"
  cat docs/codex-consolidator-prompt.md
} | ROUND="$R" timeout "$WORKER_TIMEOUT" "${CODEX[@]}" - \
    > "logs/round-${R}-consolidator.log" 2>&1 \
  && echo "== round $R DONE. New commit:" && git log --oneline -1 \
  || { echo "!! consolidator exited nonzero — see logs/round-${R}-consolidator.log"; exit 1; }
