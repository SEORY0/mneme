#!/usr/bin/env bash
# test_runner_batch.sh LABEL TASKFILE — the REAL TEST RUNNER (production solve path).
#
# Runs mneme's actual agent pipeline on each task in TASKFILE and reports solved/total.
# This MEASURES; it never learns. See docs/pipelines.md for the learning-vs-test boundary.
#
#   pipeline per task: runner/run.py solve --task-id <id> --run-dir <rd> --model <MODEL>
#     MODEL=claude-opus-4-8 (default) => MAIN agent = Claude Opus (Claude Agent SDK)
#                                        + GPT-5.5 SPECIALIST + memory/verify MCP servers
#     => real Anthropic (Opus) + OpenAI (gpt-5.5 specialist) API spend.
#   each solve: gen(level1) -> agent -> tier-1 verify -> single OFFICIAL submit -> result.json
#   `solved` in result.json is SERVER-authoritative (official vul_exit!=0 && fix_exit==0).
#
# NOT the learning pipeline: run_pass.sh / run_round.sh drive headless *Codex* workers
# (docs/codex-worker-prompt.md) that solve with NO LLM API inside mneme and write traces the
# consolidator promotes into okf memory. THIS harness imports no learning code, writes no
# memory, never consolidates — it only scores the current memory+code on a fixed task list.
#
# Env: MODEL (default claude-opus-4-8), CONC (parallel solves, default 4),
#      SOLVE_TIMEOUT (s/task, default 600).
set -uo pipefail
LABEL="${1:?usage: test_runner_batch.sh LABEL TASKFILE}"; TASKFILE="${2:?}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$REPO"; mkdir -p logs
# Opus 4.6 (NOT 4.8): 4.8 refuses the authorized CyberGym PoC task under cyber-safeguards.
MODEL="${MODEL:-claude-opus-4-6}"; CONC="${CONC:-4}"; SOLVE_TIMEOUT="${SOLVE_TIMEOUT:-600}"
OUT="runs/test_${LABEL}"; mkdir -p "$OUT"; SUMMARY="$OUT/summary.jsonl"
ts(){ date +%H:%M:%S; }; log(){ echo "[$(ts)] $*"; }
safe_task(){ printf '%s' "$1" | tr ':/' '__'; }
mapfile -t TASKS < <(grep -vE '^[[:space:]]*(#|$)' "$TASKFILE" | sed 's/[[:space:]]//g')
log "TEST RUNNER: ${#TASKS[@]} tasks, model=$MODEL, conc=$CONC, timeout=${SOLVE_TIMEOUT}s -> $OUT"

solve_one(){
  local tid="$1" safe rd rc; safe="$(safe_task "$tid")"; rd="$OUT/$safe"
  rm -rf "$rd"; mkdir -p "$rd"
  timeout "$SOLVE_TIMEOUT" .venv/bin/python runner/run.py solve \
      --task-id "$tid" --model "$MODEL" --run-dir "$rd" > "logs/test_${LABEL}_${safe}.log" 2>&1
  rc=$?
  .venv/bin/python - "$tid" "$rd/result.json" "$rc" <<'PY' >> "$SUMMARY"
import json,os,sys
tid,p,rc=sys.argv[1],sys.argv[2],int(sys.argv[3])
r=json.load(open(p)) if os.path.exists(p) else {}
print(json.dumps({"task_id":tid,"solved":bool(r.get("solved")),"target_match":r.get("target_match"),
 "failure_class":r.get("failure_class"),"submit_reason":r.get("submit_reason"),
 "vul_exit":r.get("official_vul_exit"),"fix_exit":r.get("official_fix_exit"),"rc":rc}))
PY
  log "  $tid -> $(tail -1 "$SUMMARY")"
}

: > "$SUMMARY"
running=0
for tid in "${TASKS[@]}"; do
  solve_one "$tid" &
  running=$((running+1))
  if [ "$running" -ge "$CONC" ]; then wait -n 2>/dev/null || wait; running=$((running-1)); fi
done
wait

.venv/bin/python - "$SUMMARY" "${#TASKS[@]}" <<'PY'
import json,sys
rows=[json.loads(l) for l in open(sys.argv[1]) if l.strip()]
total=int(sys.argv[2]); solved=[r for r in rows if r.get("solved")]
print("="*64)
print(f"TEST RUNNER RESULT: SOLVED {len(solved)}/{total}  ({100*len(solved)/max(total,1):.1f}%)")
print("SOLVED: "+(" ".join(r["task_id"] for r in solved) or "none"))
miss=[r["task_id"] for r in rows if not r.get("solved")]
print("FAILED: "+(" ".join(miss) or "none"))
nores=total-len(rows)
if nores>0: print(f"(no result.json for {nores} task(s) — check logs)")
print("="*64)
PY
