#!/usr/bin/env bash
# run_ablation.sh — isolate the MEMORY effect on a FIXED task set.
#
# Re-solves the same tasks under two okf versions, with the SAME current code/prompt/tooling
# (only memory differs), so the delta = the accumulated memory's contribution:
#   baseline = round-1 okf snapshot (commit 86db7c8, 44 files) — "before mode-B learning"
#   current  = HEAD okf (accumulated)
# Read-only on memory; ablation traces are NOT fed back into learning. Restores current memory
# on exit (even on failure) via a trap.
#
# NOTE: round-1's tasks were LEARNED FROM, so this is the recall-tinged UPPER BOUND of memory
# value, not a clean generalization estimate (use a held-out task list for that).
#
# Usage: run_ablation.sh [BASELINE_COMMIT] [TASKLIST_GLOB]
#   BASELINE_COMMIT  default 86db7c8 (round-1 start)
#   TASKLIST_GLOB    default 'learning/round-1/shard-*.txt' (round-1's 50 tasks)
# Cost: solves |tasks| TWICE (50 tasks => 100 headless solves). Override TASKLIST for a subset.
set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"; cd "$REPO"
BASE_COMMIT="${1:-86db7c8}"
TASKGLOB="${2:-learning/round-1/shard-*.txt}"
WORKERS=5
WORKER_TIMEOUT="${WORKER_TIMEOUT:-3600}"
mkdir -p logs

# Guard 1: never run during an active round/consolidator (memory swap would corrupt it).
if pgrep -f "codex exec" >/dev/null 2>&1; then
  echo "!! codex exec active — a round/consolidator is running. Refusing (memory swap unsafe)."; exit 1
fi
# Guard 2: memory tree must be clean (so the trap can restore cleanly).
if ! git diff --quiet -- memory_store/okf memory_store/memory_stats.jsonl; then
  echo "!! memory_store has uncommitted changes; commit them before ablation."; exit 1
fi

CODEX=(codex exec --dangerously-bypass-approvals-and-sandbox -C "$REPO" -c shell_environment_policy.inherit=all)
[ -n "${CODEX_MODEL:-}" ] && CODEX+=(-m "$CODEX_MODEL")

mapfile -t TASKS < <(cat $TASKGLOB 2>/dev/null | sed 's/#.*//' | tr -s ' \t' '\n' | grep -E '^[a-z]+:' | sort -u)
[ "${#TASKS[@]}" -gt 0 ] || { echo "no tasks from glob: $TASKGLOB"; exit 1; }
echo "ablation: ${#TASKS[@]} tasks  baseline=$BASE_COMMIT  (solves twice => $(( ${#TASKS[@]} * 2 )) total)"

make_shards() {  # tag — split TASKS round-robin into pseudo-round shards
  local tag="$1" i=0 k t
  rm -rf "learning/round-$tag"; mkdir -p "learning/round-$tag/traces"
  for t in "${TASKS[@]}"; do k=$(( i % WORKERS + 1 )); echo "$t" >> "learning/round-$tag/shard-$k.txt"; i=$((i+1)); done
}

run_condition() {  # tag
  local tag="$1" pids=() k
  make_shards "$tag"
  for k in $(seq 1 $WORKERS); do
    { printf 'Use WORKER_ID=%s and ROUND=%s. Solve ONLY learning/round-%s/shard-%s.txt. Do NOT run shard_round. This is an ABLATION re-solve; write traces normally to learning/round-%s/traces/.\n\n' "$k" "$tag" "$tag" "$k" "$tag"
      cat docs/codex-worker-prompt.md
    } | WORKER_ID="$k" ROUND="$tag" timeout "$WORKER_TIMEOUT" "${CODEX[@]}" - > "logs/ablation-$tag-worker-$k.log" 2>&1 &
    pids+=($!); sleep 10
  done
  for p in "${pids[@]}"; do wait "$p" || true; done
}

tally() {  # tag -> prints "solved/total" and a per-range line
  python3 - "$1" <<'PY'
import json,glob,sys
sys.path.insert(0,"scripts/learning"); import _common as C
tag=sys.argv[1]
ts=[json.load(open(p)) for p in glob.glob(f"learning/round-{tag}/traces/*.json")]
recs=[{"task_id":d.get("task_id"),"solved":d.get("solved")} for d in ts]
agg=C.aggregate_by_range(recs)
s=agg["TOTAL"]["wins"]; n=agg["TOTAL"]["attempted"]
print(f"{s}/{n}")
for k,v in agg.items():
    if k!="TOTAL": print(f"    {k}: {v['wins']}/{v['attempted']}")
PY
}

# Backup current memory; restore on ANY exit.
BK="$(mktemp -d)"; cp -a memory_store/okf "$BK/okf"; cp -a memory_store/memory_stats.jsonl "$BK/stats" 2>/dev/null || true
restore_current() {
  rm -rf memory_store/okf; cp -a "$BK/okf" memory_store/okf
  [ -f "$BK/stats" ] && cp -a "$BK/stats" memory_store/memory_stats.jsonl
  git checkout -- memory_store/okf memory_store/memory_stats.jsonl 2>/dev/null || true
}
trap restore_current EXIT

echo "== condition: CURRENT memory (HEAD) =="
run_condition "ablo-cur"; CUR="$(tally ablo-cur)"

echo "== condition: BASELINE memory ($BASE_COMMIT) =="
rm -rf memory_store/okf
git archive "$BASE_COMMIT" -- memory_store/okf | tar -x
git show "$BASE_COMMIT:memory_store/memory_stats.jsonl" > memory_store/memory_stats.jsonl 2>/dev/null || : > memory_store/memory_stats.jsonl
run_condition "ablo-base"; BASE="$(tally ablo-base)"
restore_current; trap - EXIT

echo
echo "==== ABLATION (memory-only, same code/prompt; round-1 tasks = recall-tinged UPPER BOUND) ===="
printf '  baseline okf (%s): %s\n' "$BASE_COMMIT" "$BASE"
printf '  current  okf (HEAD):  %s\n' "$CUR"
echo "  recorded round-1 (reference, old prompt): 6/50"
echo "  (ablation pseudo-rounds left in learning/round-ablo-* — rm -rf when done)"
