#!/bin/bash
cd /home/nsd/mneme
SUM=runs/subset10_g55_results.jsonl; : > "$SUM"
while read -r tid; do
  [ -z "$tid" ] && continue
  safe=$(echo "$tid" | tr ':/' '__'); rd="runs/g55_$safe"
  echo "===== $tid -> $rd $(date -u +%H:%M:%S) ====="
  rm -rf "$rd"
  timeout 900 .venv/bin/python runner/run.py solve --task-id "$tid" --model gpt-5.5 --run-dir "$rd" > "logs/g55_$safe.log" 2>&1
  rc=$?
  python3 -c "
import json,os
p='$rd/result.json'
r=json.load(open(p)) if os.path.exists(p) else {}
r['task_id']='$tid'; r['exit_rc']=$rc
print(json.dumps({k:r.get(k) for k in ['task_id','solved','target_match','failure_class','official_vul_exit','official_fix_exit','submit_reason','exit_rc']}))
" >> "$SUM"
  echo "  $(tail -1 $SUM)"
done < data/subset10.txt
echo "===== DONE $(date -u +%H:%M:%S) ====="
