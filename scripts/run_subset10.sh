#!/bin/bash
# Live 10-subset run. Records each result.json + a summary JSONL. Honest capture
# (including cyber-safeguard refusals). No safety bypass attempted.
cd /home/nsd/mneme
SUMMARY=runs/subset10_results.jsonl
: > "$SUMMARY"
while read -r tid; do
  [ -z "$tid" ] && continue
  safe=$(echo "$tid" | tr ':/' '__')
  rd="runs/$safe"
  echo "===== $tid -> $rd $(date -u +%H:%M:%S) ====="
  timeout 300 .venv/bin/python runner/run.py solve --task-id "$tid" --run-dir "$rd" > "logs/$safe.log" 2>&1
  rc=$?
  # extract stop_reason from transcript if present
  stop=$(grep -o "stop_reason='[a-z_]*'" "$rd/transcript.txt" 2>/dev/null | tail -1)
  res=$(cat "$rd/result.json" 2>/dev/null | tr -d '\n')
  python3 -c "import json,sys;
r=json.load(open('$rd/result.json')) if __import__('os').path.exists('$rd/result.json') else {}
r['task_id']='$tid'; r['exit_rc']=$rc; r['agent_stop']='$stop'
print(json.dumps(r))" >> "$SUMMARY"
  echo "  rc=$rc stop=$stop result=$res"
done < data/subset10.txt
echo "===== DONE $(date -u +%H:%M:%S) ====="
