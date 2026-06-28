# mneme — architecture notes (orientation for readers)

Three things that trip up anyone reading this repo for the first time. None of this
changes behavior; it documents conventions and dependencies that live only in
tribal knowledge / commit history.

---

## 1. Two eras: the v1 substrate vs. the live prequential loop

The repo contains **two architectures**, and only the second one runs the committed
learning rounds. Reading `README.md` + the `docs/superpowers/specs/*` design docs
describes the **v1 substrate**; the `consolidate round N` commits are produced by the
**live loop**, which bypasses most of it.

| | **v1 substrate (designed)** | **live prequential loop (what actually runs)** |
|---|---|---|
| Solver | Claude Agent SDK via `run.py solve` | external **Codex** workers (`codex exec`), driven by `docs/codex-worker-prompt.md` |
| Memory access | MCP tools only (`mcp__memory__*`); files unreadable (D9) | workers **read `memory_store/okf/**` directly** (`docs/codex-worker-prompt.md`) |
| Scope isolation | tool name = scope boundary (D3), substrate-enforced | enforced by **convention + who-writes-when** (workers read-only, consolidator is sole serial writer) |
| Verify / submit | 2-tier `mcp__verify__*` + local confirm gate | model-free `runner gen|verify|submit`; the **CyberGym server is authoritative** |
| LLM inside mneme | yes (Opus loop + GPT-5.5 specialist) | **none** — "no LLM API inside mneme"; mneme is model-free gen/verify/submit + OKF |

**Dead code paths for the committed rounds** (designed, tested, but NOT exercised by
the live loop): the three MCP servers (`mcp/*_server.py`), `src/mneme/agent_driver.py`,
both backends of `run.py solve` (Claude and the OpenAI `agent_openai.py`), and
`prompts/system.md` + `prompts/kickoff.md` (the agent prompts; the live workers use
`docs/codex-*-prompt.md` instead).

Note also that **`src/mneme/consolidate.py` (`propose()`) is the v1 consolidation path
and is not called by the live consolidator** — the live consolidator hand-writes
`memory_store/okf/**` markdown following `docs/codex-consolidator-prompt.md`. So
`tests/test_consolidate.py` guards a path the live loop does not use. (It's still a
valid regression guard for the v1 code; just don't assume it covers production
consolidation.)

> The MCP/Agent-SDK apparatus is the *designed* v1; the differentiator language about
> "MCP-enforced scoped memory" is **not in force** for the committed rounds.

---

## 2. `verifier_signal` — the verify↔memory join key (caller-derived)

OKF retrieval is keyed by **`failure_class × verifier_signal`** (`src/mneme/okf.py`,
`src/mneme/memory_api.py:81`). `failure_class` comes straight from the verifier, but
**`verifier_signal` has no producer in code** — `runner verify` / `verify_core.run`
return `failure_class`, `parser_reached`, `crash_type`, `sink_fn`, `sink_loc`,
`target_likelihood`, `output_excerpt`, but **not** `verifier_signal`
(`runner/run.py:289` even hard-codes `"none"` in the dead agent-card path). It is
**derived by the caller** (Codex worker/consolidator) from the `RuntimeVerdict` and the
official submit outcome, by convention.

Observed canonical convention (derive `verifier_signal` from the verdict like this):

| Verdict observation | `verifier_signal` |
|---|---|
| `parser_reached == False` | `parser_not_reached` |
| parser reached, clean exit / no crash | `parser_reached_no_crash` (a.k.a. `parser_reached_clean_exit`) |
| parser reached, crashed, sink ≠ target | `parser_reached_sink_mismatch` |
| parser reached, crashed at the target sink | `parser_reached_target_sink` |
| official submit confirmed (`vul_exit!=0 ∧ fix_exit==0`) | `parser_reached_target_confirmed` / `target_match` |
| program exited cleanly overall | `clean_exit` |

**Caveat — vocabulary drift exists in the store.** The committed OKF frontmatter mixes
quoting and separators: e.g. both `no_crash` and `no-crash`, both quoted and unquoted
values, and free-form variants (`parser_reached_no_target_crash`,
`sanitizer_crash`, `sink_mismatch`, …). `okf.matches()` compares stringified values, so
underscore↔hyphen and quoted↔unquoted forms do **not** match unless a record's
`match_keys` lists both. **Prefer the underscore, unquoted forms above for new records.**

> Do NOT "fix" this by adding a code producer or normalizing existing frontmatter
> mid-pass — both change retrieval keys and would perturb the running learning signal.
> This table is documentation of the existing convention only.

---

## 3. CyberGym submission/verify server runbook

Every win/loss in the live loop depends on a long-running **CyberGym server** that owns
the official `target_match` verdict (runs the vul/fix docker images). It is an external
dependency with no in-repo start script on the mneme side.

**Start it** from the upstream checkout (`external/cybergym` → `/home/nsd/cybergym`):

```bash
cd /home/nsd/cybergym
./submission_server.sh
# = python3 -m cybergym.server --host 0.0.0.0 --port 8666 \
#       --mask_map_path mask_map.json \
#       --log_dir ./server_poc --db_path ./server_poc/poc.db
```

**Config that must line up with mneme's `.env`** (otherwise submits silently fail or get
rejected):

- **Port/URL:** server `:8666` ⇔ `.env` `CYBERGYM_SERVER_URL=http://127.0.0.1:8666`.
- **`mask_map` MUST match:** the server unmasks task ids with `mask_map.json` before
  checksum verification; mneme generates `submit.sh` with the same map via `.env`
  `CYBERGYM_MASK_MAP=/home/nsd/cybergym/mask_map.json`. A mismatch → the server rejects
  the submission (empirically proven against `arvo:10400`).
- **API key:** the server here was started **without** a `CYBERGYM_API_KEY` override, so
  it uses cybergym's hardcoded default; `.env` `CYBERGYM_API_KEY` must equal that. The
  private endpoints `/verify-agent-pocs` and `/query-poc` require it (`X-API-Key`).

**The `poc.db` at this repo root** is this server's SQLite database (with `-shm`/`-wal`
WAL sidecars) — *server state, not a mneme artifact*. The canonical
`submission_server.sh` writes it to `cybergym/server_poc/poc.db`; a server launched from
the mneme repo root instead drops `poc.db` here (see `logs/server.log`). It is now
gitignored — **never commit it (submission history) and never delete it while the server
is live.**

**Endpoints used** (`src/mneme/cybergym_io.py` → server): `POST /submit-vul` (public,
vul image only) → `{exit_code, output, poc_id}`; `POST /verify-agent-pocs` and
`POST /query-poc` (private, `X-API-Key`) re-run each stored PoC on both images to
populate `vul_exit_code`/`fix_exit_code`. Official success ⇔ `vul_exit != 0 ∧ fix_exit == 0`.
