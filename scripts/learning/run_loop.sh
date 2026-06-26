#!/usr/bin/env bash
# run_loop.sh START END [WORKERS] [BATCH] — run mode-B rounds START..END unattended.
#
# Calls run_round.sh per round (shard -> parallel headless workers -> consolidator commit).
# Stops early if a round fails to complete. Optionally pushes after each kept round.
#
# Env: ROUND_GAP (s between rounds, default 30), PUSH_EACH=1 to `git push` after each round.
set -uo pipefail

START="${1:?usage: run_loop.sh START END [WORKERS] [BATCH]}"
END="${2:?usage: run_loop.sh START END [WORKERS] [BATCH]}"
WORKERS="${3:-5}"
BATCH="${4:-50}"
GAP="${ROUND_GAP:-30}"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for ((R=START; R<=END; R++)); do
  echo "######## ROUND $R ($(date +%T)) ########"
  if ! bash "$DIR/run_round.sh" "$R" "$WORKERS" "$BATCH"; then
    echo "!! round $R failed — stopping loop at round $R."
    exit 1
  fi
  [ "${PUSH_EACH:-0}" = "1" ] && git push 2>&1 | tail -2
  [ "$R" -lt "$END" ] && sleep "$GAP"
done
echo "######## loop done (rounds $START..$END) ########"
