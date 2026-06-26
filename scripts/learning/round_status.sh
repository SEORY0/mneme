#!/usr/bin/env bash
# round_status.sh <R> — per-worker progress for a learning round.
#
# For each shard-W.txt, count assigned task ids vs trace JSONs present, print
# per-worker progress, and report whether the round is COMPLETE (every assigned
# task across all shards has a trace). Exit 0 if complete, 1 otherwise.
set -euo pipefail

R="${1:-}"
if [[ -z "$R" ]]; then
  echo "usage: $0 <round>" >&2
  exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
ROUND_DIR="$REPO_ROOT/learning/round-$R"
TRACES_DIR="$ROUND_DIR/traces"

if [[ ! -d "$ROUND_DIR" ]]; then
  echo "no such round dir: $ROUND_DIR (run shard_round.py --round $R first)" >&2
  exit 2
fi

safe_task() { printf '%s' "$1" | tr ':/' '__'; }

total_assigned=0
total_traces=0

echo "Round $R status ($ROUND_DIR):"
for shard in "$ROUND_DIR"/shard-*.txt; do
  [[ -e "$shard" ]] || continue
  w="$(basename "$shard" .txt)"
  assigned=0
  have=0
  while IFS= read -r task; do
    task="${task%%#*}"
    task="$(printf '%s' "$task" | xargs)"
    [[ -z "$task" ]] && continue
    assigned=$((assigned + 1))
    st="$(safe_task "$task")"
    if [[ -f "$TRACES_DIR/$st.json" ]]; then
      have=$((have + 1))
    fi
  done < "$shard"
  total_assigned=$((total_assigned + assigned))
  total_traces=$((total_traces + have))
  status="in-progress"
  [[ "$have" -ge "$assigned" && "$assigned" -gt 0 ]] && status="DONE"
  printf '  %-9s %2d/%-2d traces  [%s]\n' "$w" "$have" "$assigned" "$status"
done

echo "  ----"
printf '  TOTAL    %d/%d traces\n' "$total_traces" "$total_assigned"

if [[ "$total_assigned" -gt 0 && "$total_traces" -ge "$total_assigned" ]]; then
  echo "  ROUND COMPLETE — ready for the consolidator."
  exit 0
else
  echo "  ROUND INCOMPLETE — wait for workers."
  exit 1
fi
