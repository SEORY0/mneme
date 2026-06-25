# memonaemo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build memonaemo — a single Claude (Opus 4.8) agent that solves CyberGym Level-1 PoC tasks, where skills/OKF are markdown, memory and verification are MCP tools, a GPT-5.5 specialist is an MCP advisor, and Python is only a thin runner — beating Crystalline via verification-gated, scope-isolated causal memory.

**Architecture:** Python Claude Agent SDK drives the agent loop. Three local MCP servers (`memory`, `verify`, `specialist`) expose tools; OKF/causal memory lives in `memory_store/` outside the agent's filesystem reach (D9). The runner prepares a redacted task card, launches the agent, performs the single official `submit.sh`, and runs offline verifier-gated consolidation. Proven logic (docker verify, submit parsing, redaction, causal keying) is **ported from `/home/nsd/SCHE-MA/schema/simple-memory`**, not rewritten.

**Tech Stack:** Python 3.12; `claude-agent-sdk` 0.2.103; `anthropic` 0.109.2; `openai` 2.43.0; `mcp` (stdio servers); `pytest`; Docker (cybergym `cybergym/oss-fuzz` `<id>-vul` / `<id>-fix` images); Typer CLI.

## Global Constraints

- Python is runner + MCP + tool glue ONLY. No operating procedure or policy playbook in Python — those live in `memory_store/okf/**` markdown or `skills/**`.
- Agent model: `claude-opus-4-8`. Specialist model: GPT-5.5 (resolve exact OpenAI model id at implementation time via `openai` client; do not hardcode a guessed string — see Task 8).
- D3: scope = tool name. No `scope` argument on memory tools.
- D9: the agent's filesystem tools (Read/Grep/Glob/Bash) are confined to the run workspace + `skills/`. `memory_store/**` is NEVER agent-readable; OKF reaches the agent only through `memory.*` tool results.
- D11: redaction strictness applies at long-term promotion only. Run-local solve context may contain repo-discovered function names / lines / sinks. Forbidden in any promotion: raw PoC bytes, task-id-keyed facts, submit metadata, server URLs, agent ids, checksums, exact offsets.
- Verify signal split: `verify.run` (vul image) may only emit `no_crash` | `bad_format` | `wrong_sink` | `generic_crash` + `target_likelihood`. `both_crash` / `post_patch_crash` / confirmed `target_match` come ONLY from `verify.confirm_if_available` (vul+fix) or final submit.
- Consolidation: offline, train-only, dry-run by default; eval-split tasks refused.
- Source of truth for ported logic: `/home/nsd/SCHE-MA/schema/simple-memory/simple_memory/`. Spec: `docs/superpowers/specs/2026-06-25-memonaemo-design.md`.
- Run all Python via the repo venv created in Task 1; run pytest with `PYTHONPATH=src`.

---

### Task 1: Project scaffold + pinned deps + smoke test

**Files:**
- Create: `pyproject.toml`
- Create: `src/memonaemo/__init__.py`
- Create: `tests/test_smoke.py`
- Create: `.gitignore`

**Interfaces:**
- Produces: importable package `memonaemo` (version string `__version__`); a venv at `.venv`.

- [ ] **Step 1: Write `pyproject.toml`**

```toml
[project]
name = "memonaemo"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "claude-agent-sdk==0.2.103",
  "anthropic>=0.109,<0.110",
  "openai>=2.43,<3",
  "mcp>=1.0",
  "typer>=0.12",
]
[project.optional-dependencies]
dev = ["pytest>=7.4"]

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
```

- [ ] **Step 2: Write the package init**

`src/memonaemo/__init__.py`:
```python
__version__ = "0.1.0"
```

- [ ] **Step 3: Write `.gitignore`**

```
.venv/
__pycache__/
*.pyc
runs/
memory_store/memory_stats.jsonl
.env
```

- [ ] **Step 4: Write the smoke test**

`tests/test_smoke.py`:
```python
import memonaemo

def test_version():
    assert memonaemo.__version__ == "0.1.0"
```

- [ ] **Step 5: Create venv and install**

Run: `python3.12 -m venv .venv && .venv/bin/pip install -e '.[dev]'`
Expected: install succeeds (claude-agent-sdk, anthropic, openai, mcp, typer resolve).

- [ ] **Step 6: Run the smoke test**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_smoke.py -v`
Expected: 1 passed.

- [ ] **Step 7: Commit**

```bash
git add pyproject.toml src/memonaemo/__init__.py tests/test_smoke.py .gitignore
git commit -m "chore: scaffold memonaemo package and deps"
```

---

### Task 2: Curated import of OKF + skills + split, with leak audit

**Files:**
- Create: `memory_store/okf/**` (copied from `/home/nsd/SCHE-MA/skills/knowledge/okf/**`)
- Create: `skills/tools/**`, `skills/shared/**` (copied from `/home/nsd/SCHE-MA/skills/{tools,shared}/**`)
- Create: `data/okf_split.json` (copied from `/home/nsd/SCHE-MA/data/okf_split.json`)
- Create: `tests/test_okf_hygiene.py`
- Create: `scripts/audit_leak.py`

**Interfaces:**
- Produces: `memory_store/okf/index.md` and typed subdirs (`vuln-classes/`, `formats/`, `strategies/`, `causal-policies/`); agent-readable `skills/tools/*.md`, `skills/shared/*.md`.

- [ ] **Step 1: Write the leak-audit failing test**

`tests/test_okf_hygiene.py`:
```python
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Real CyberGym task ids look like arvo:NNNNN or oss-fuzz numeric ids.
FORBIDDEN = [
    re.compile(r"arvo:\d+"),
    re.compile(r"\b\d{8,}-(?:vul|fix)\b"),  # oss-fuzz image tags
    re.compile(r"submit-vul"),
    re.compile(r"\bchecksum\b\s*[:=]\s*[0-9a-f]{8,}", re.I),
]

def _md_files():
    for base in ("memory_store/okf", "skills"):
        yield from (ROOT / base).rglob("*.md")

def test_no_taskid_or_submit_leak_in_okf():
    offenders = []
    for f in _md_files():
        text = f.read_text(encoding="utf-8")
        for pat in FORBIDDEN:
            if pat.search(text):
                offenders.append(f"{f}: {pat.pattern}")
    assert not offenders, offenders

def test_okf_index_present():
    assert (ROOT / "memory_store/okf/index.md").is_file()
```

- [ ] **Step 2: Run it to verify it fails**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_okf_hygiene.py -v`
Expected: FAIL (`memory_store/okf/index.md` missing).

- [ ] **Step 3: Copy OKF, skills, split**

```bash
mkdir -p memory_store skills data
cp -r /home/nsd/SCHE-MA/skills/knowledge/okf memory_store/okf
cp -r /home/nsd/SCHE-MA/skills/tools skills/tools
cp -r /home/nsd/SCHE-MA/skills/shared skills/shared
cp /home/nsd/SCHE-MA/data/okf_split.json data/okf_split.json
# Drop any provenance/local files that may carry private markers:
rm -f memory_store/okf/_provenance.local.md
```

- [ ] **Step 4: Write `scripts/audit_leak.py`** (reusable CLI wrapper around the same patterns)

```python
"""Scan a directory tree of markdown for task-id / submit-metadata leakage."""
import re, sys
from pathlib import Path

PATTERNS = [r"arvo:\d+", r"\b\d{8,}-(?:vul|fix)\b", r"submit-vul"]

def main(root: str) -> int:
    rx = [re.compile(p) for p in PATTERNS]
    bad = []
    for f in Path(root).rglob("*.md"):
        t = f.read_text(encoding="utf-8")
        for r in rx:
            if r.search(t):
                bad.append(f"{f}: {r.pattern}")
    for b in bad:
        print(b)
    return 1 if bad else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "memory_store/okf"))
```

- [ ] **Step 5: Run the audit and the test**

Run: `.venv/bin/python scripts/audit_leak.py memory_store/okf && PYTHONPATH=src .venv/bin/pytest tests/test_okf_hygiene.py -v`
Expected: audit prints nothing (exit 0); both tests pass. If the audit flags a file, redact the offending token in that markdown (abstract it) before continuing.

- [ ] **Step 6: Add frontmatter scope fields to causal policies**

For each file in `memory_store/okf/causal-policies/*.md`, ensure the YAML frontmatter contains: `allowed_scopes`, `forbidden_fields`, `evidence_level`, `train_only`. Example addition to `bad-format-repair.md` frontmatter:
```yaml
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
```
(Map existing `confidence` → `evidence_level`; `access_scope: generate` → `allowed_scopes: [generate]`.)

- [ ] **Step 7: Commit**

```bash
git add memory_store/okf skills data/okf_split.json tests/test_okf_hygiene.py scripts/audit_leak.py
git commit -m "feat: curated OKF/skills import with leak audit and scope frontmatter"
```

---

### Task 3: OKF loader + keyed retrieval ranking (no vectors) + stats sidecar

**Files:**
- Create: `src/memonaemo/okf.py`
- Create: `src/memonaemo/stats.py`
- Create: `tests/test_okf_loader.py`

**Interfaces:**
- Produces:
  - `okf.load_policies(store_dir: Path) -> list[Policy]` where `Policy` is a dataclass with `name: str`, `body: str`, `match_keys: list[str]`, `allowed_scopes: list[str]`, `evidence_level: str`, `train_only: bool`, plus the full frontmatter `meta: dict`.
  - `okf.compact_record(p: Policy) -> dict` returning only `{name, policy, procedure, negative_memory, evidence_level}` text sections — NEVER the full body (D: `get_repair_policy` returns compact record only).
  - `okf.rank(policies, query: dict, stats: Stats) -> list[Policy]` ordered by the weighted score below.
  - `stats.Stats.load(path)`, `stats.Stats.success_rate(policy_name) -> float`, `stats.Stats.frequency(policy_name) -> int`, `stats.Stats.recency_rank(policy_name) -> int`, `stats.Stats.record(path, policy_name, *, success: bool)` appending one JSON line to `memory_stats.jsonl`.

- [ ] **Step 1: Write failing tests**

`tests/test_okf_loader.py`:
```python
from pathlib import Path
from memonaemo import okf, stats

STORE = Path(__file__).resolve().parents[1] / "memory_store"

def test_load_policies_have_match_keys():
    ps = okf.load_policies(STORE)
    assert ps
    assert any("bad_format" in p.match_keys for p in ps)

def test_compact_record_excludes_full_body():
    ps = okf.load_policies(STORE)
    p = next(p for p in ps if "bad_format" in p.match_keys)
    rec = okf.compact_record(p)
    assert set(rec) <= {"name", "policy", "procedure", "negative_memory", "evidence_level"}
    assert "## Evidence Shape" not in rec.get("policy", "")  # not the raw body

def test_rank_prefers_higher_success_rate(tmp_path):
    st = stats.Stats.load(tmp_path / "s.jsonl")
    ps = okf.load_policies(STORE)
    # Two policies that both match the query; success-rate must dominate text order.
    q = {"failure_class": "bad_format", "verifier_signal": "parser_not_reached"}
    matched = [p for p in ps if okf.matches(p, q)]
    assert matched, "expected at least one matching policy"
    name = matched[0].name
    stats.Stats.record(tmp_path / "s.jsonl", name, success=True)
    st2 = stats.Stats.load(tmp_path / "s.jsonl")
    ranked = okf.rank(ps, q, st2)
    assert ranked[0].name == name

def test_rank_is_not_text_similarity():
    # rank() must not import or use any embedding / vector lib.
    import inspect, memonaemo.okf as m
    src = inspect.getsource(m)
    assert "embedding" not in src.lower() and "cosine" not in src.lower()
```

- [ ] **Step 2: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_okf_loader.py -v`
Expected: FAIL (module `memonaemo.okf` not found).

- [ ] **Step 3: Implement `stats.py`**

```python
from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class Stats:
    rows: list[dict] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path) -> "Stats":
        p = Path(path)
        if not p.exists():
            return cls()
        rows = [json.loads(line) for line in p.read_text().splitlines() if line.strip()]
        return cls(rows)

    @staticmethod
    def record(path: Path, policy_name: str, *, success: bool) -> None:
        line = json.dumps({"policy": policy_name, "success": bool(success)})
        with Path(path).open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")

    def _for(self, name: str) -> list[dict]:
        return [r for r in self.rows if r.get("policy") == name]

    def success_rate(self, name: str) -> float:
        rs = self._for(name)
        if not rs:
            return 0.0
        return sum(1 for r in rs if r.get("success")) / len(rs)

    def frequency(self, name: str) -> int:
        return len(self._for(name))

    def recency_rank(self, name: str) -> int:
        # Higher = more recently used. Index of last occurrence.
        last = -1
        for i, r in enumerate(self.rows):
            if r.get("policy") == name:
                last = i
        return last
```

- [ ] **Step 4: Implement `okf.py`**

```python
from __future__ import annotations
import re
from dataclasses import dataclass
from pathlib import Path

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

@dataclass
class Policy:
    name: str
    body: str
    match_keys: list[str]
    allowed_scopes: list[str]
    evidence_level: str
    train_only: bool
    meta: dict

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    m = _FRONTMATTER.match(text)
    if not m:
        return {}, text
    import_yaml = __import__("yaml") if _has_yaml() else None
    raw, body = m.group(1), m.group(2)
    meta = import_yaml.safe_load(raw) if import_yaml else _mini_yaml(raw)
    return (meta or {}), body

def _has_yaml() -> bool:
    try:
        __import__("yaml"); return True
    except Exception:
        return False

def _mini_yaml(raw: str) -> dict:
    # Minimal key: value / key: [a, b] parser, used only if PyYAML absent.
    out: dict = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            out[k.strip()] = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        else:
            out[k.strip()] = v.strip("\"'")
    return out

def load_policies(store_dir: Path) -> list[Policy]:
    pol_dir = Path(store_dir) / "okf" / "causal-policies"
    policies: list[Policy] = []
    for f in sorted(pol_dir.glob("*.md")):
        meta, body = _parse_frontmatter(f.read_text(encoding="utf-8"))
        keys = list(meta.get("match_keys") or meta.get("tags") or [])
        policies.append(Policy(
            name=f.stem, body=body, match_keys=keys,
            allowed_scopes=list(meta.get("allowed_scopes", ["generate"])),
            evidence_level=str(meta.get("evidence_level", meta.get("confidence", "low"))),
            train_only=bool(meta.get("train_only", True)),
            meta=meta,
        ))
    return policies

def matches(p: Policy, query: dict) -> bool:
    wanted = {str(v) for v in query.values() if v}
    return bool(wanted & set(p.match_keys)) or any(
        str(query.get(k)) == str(p.meta.get(k)) for k in ("failure_class", "verifier_signal", "input_format", "harness_convention", "vuln_class")
        if query.get(k)
    )

def _section(body: str, header: str) -> str:
    m = re.search(rf"^##\s+{re.escape(header)}\s*\n(.*?)(?=^##\s|\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""

def compact_record(p: Policy) -> dict:
    return {
        "name": p.name,
        "policy": _section(p.body, "Policy"),
        "procedure": _section(p.body, "Procedure"),
        "negative_memory": _section(p.body, "Negative Memory"),
        "evidence_level": p.evidence_level,
    }

_EVIDENCE = {"high": 1.0, "medium": 0.6, "low": 0.3}

def rank(policies: list[Policy], query: dict, stats) -> list[Policy]:
    def score(p: Policy) -> tuple:
        if not matches(p, query):
            base = -1.0
        else:
            base = 0.0
        sr = stats.success_rate(p.name)
        ev = _EVIDENCE.get(p.evidence_level, 0.3)
        freq = stats.frequency(p.name)
        rec = stats.recency_rank(p.name)
        # Weighting: success-rate dominates, then evidence, frequency, recency.
        return (base, 3.0 * sr + 1.5 * ev + 0.3 * min(freq, 10) / 10 + 0.1 * (rec >= 0))
    return sorted(policies, key=score, reverse=True)
```

(PyYAML is pulled in transitively or add `pyyaml` to deps in Task 1 if absent; the `_mini_yaml` fallback keeps tests green without it.)

- [ ] **Step 5: Run tests**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_okf_loader.py -v`
Expected: 4 passed. (If `matches`/sections don't line up with the real policy markdown, adjust the section headers to match the actual files seen in Task 2, not the test.)

- [ ] **Step 6: Commit**

```bash
git add src/memonaemo/okf.py src/memonaemo/stats.py tests/test_okf_loader.py
git commit -m "feat: keyed OKF retrieval ranking + stats sidecar (no vectors)"
```

---

### Task 4: Port task_card with redaction altitude

**Files:**
- Create: `src/memonaemo/task_card.py`
- Create: `tests/test_task_card.py`
- Reference: `/home/nsd/SCHE-MA/schema/simple-memory/simple_memory/task_card.py`, `task_redaction.py`

**Interfaces:**
- Produces:
  - `task_card.build(task_dir: Path) -> TaskCard` dataclass with fields `description: str`, `vuln_classes: list[str]`, `input_format: str`, `harness_convention: str`, `seed_hints: list[str]`, `recon: str`. Run-local recon MAY contain function names / lines / sinks (D11).
  - `task_card.redact_for_promotion(text: str) -> str` stripping task-id / submit-metadata / checksums / exact offsets — used ONLY by consolidation (Task 9), never on the card.
  - `task_card.to_markdown(card: TaskCard) -> str` for prompt injection (with the untrusted-data wrapper).

- [ ] **Step 1: Read the source modules** (`task_card.py`, `task_redaction.py`) to learn the exact redaction tokens and the `_input_format` / `atomic_vulns.classify_from_description` helpers. Port the redaction regexes verbatim into `redact_for_promotion`; do NOT apply them in `build`.

- [ ] **Step 2: Write failing tests**

`tests/test_task_card.py`:
```python
from pathlib import Path
from memonaemo import task_card

FIX = Path(__file__).resolve().parent / "fixtures" / "minimal-task"

def test_build_keeps_runlocal_sink(tmp_path):
    d = tmp_path / "t"
    d.mkdir()
    (d / "description.txt").write_text(
        "Heap buffer overflow write in parse_header at parser.c:128. TIFF input."
    )
    card = task_card.build(d)
    # D11: run-local context keeps discovered function/line/sink.
    assert "parse_header" in card.description
    assert "tiff" in card.input_format.lower()

def test_promotion_redaction_strips_offsets_and_taskids():
    txt = "arvo:12345 sink at parser.c:128 offset 0x4012 checksum a1b2c3d4e5"
    out = task_card.redact_for_promotion(txt)
    assert "arvo:12345" not in out
    assert "0x4012" not in out
    assert "a1b2c3d4e5" not in out

def test_to_markdown_wraps_untrusted():
    card = task_card.build(_make(Path("/tmp")))  # see helper note
    md = task_card.to_markdown(card)
    assert "untrusted task description data" in md
```
(Replace `_make` with the tmp_path fixture pattern from the first test; keep one canonical builder.)

- [ ] **Step 3: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_task_card.py -v`
Expected: FAIL (module missing).

- [ ] **Step 4: Implement `task_card.py`** — port `build` from simple-memory's `build_task_card` but DROP the prompt-facing redaction call on the description/recon; keep classification (`vuln_classes`, `input_format`) and the untrusted-data wrapper in `to_markdown`. Implement `redact_for_promotion` from the ported regexes plus an offset pattern `\b0x[0-9a-fA-F]+\b` and a hex-checksum pattern `\b[0-9a-f]{8,}\b`.

- [ ] **Step 5: Run tests**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_task_card.py -v`
Expected: 3 passed.

- [ ] **Step 6: Commit**

```bash
git add src/memonaemo/task_card.py tests/test_task_card.py tests/fixtures
git commit -m "feat: task_card with redaction altitude (run-local sinks allowed, strict at promotion)"
```

---

### Task 5: verify MCP server (2-tier docker) with signal split

**Files:**
- Create: `src/memonaemo/verify_core.py` (pure logic, no MCP)
- Create: `mcp/verify_server.py` (MCP stdio wrapper)
- Create: `tests/test_verify_core.py`
- Reference: `/home/nsd/SCHE-MA/schema/simple-memory/simple_memory/verifier.py`

**Interfaces:**
- Produces:
  - `verify_core.run(candidate_path, *, vul_image, run_cmd, timeout_s, description, docker=subprocess) -> RuntimeVerdict` with fields `failure_class` in `{no_crash, bad_format, wrong_sink, generic_crash}`, `crash_type`, `sink_fn`, `sink_loc`, `parser_reached`, `target_likelihood` in `{low, medium, high}`, `output_excerpt`. **Never** returns `both_crash` / `post_patch_crash` / a confirmed `target_match`.
  - `verify_core.confirm(candidate_path, *, vul_image, fix_image, run_cmd, timeout_s, description, docker=subprocess) -> ConfirmVerdict` with `available: bool`, and when available `both_crash: bool`, `post_patch_crash: bool`, `target_match: bool`. Returns `available=False` when `fix_image` is missing/unrunnable.
- Consumes: ports `parse_sanitizer`, `is_crash`, `_matches_expected_target`, sink-token logic from simple-memory's `verifier.py`.

- [ ] **Step 1: Read** simple-memory `verifier.py` for `parse_sanitizer`, `is_crash`, `infer_parser_reached`, `_matches_expected_target`, and the docker `_run`/`docker cp`/`docker exec timeout -s KILL` flow. Reuse them.

- [ ] **Step 2: Write failing tests** (inject a fake docker runner so no real Docker is needed)

`tests/test_verify_core.py`:
```python
from memonaemo import verify_core

class FakeDocker:
    def __init__(self, outputs): self.outputs = outputs; self.calls = []
    def run(self, args, timeout=None, **kw):
        self.calls.append(args)
        import types
        key = "exec" if "exec" in args else ("inspect" if "inspect" in args else "other")
        out = self.outputs.get(key, "")
        code = self.outputs.get(f"{key}_code", 0)
        return types.SimpleNamespace(returncode=code, stdout=out, stderr="")

ASAN_HEAP_WRITE = (
    "==1==ERROR: AddressSanitizer: heap-buffer-overflow ... WRITE of size 4\n"
    "    #0 0x... in parse_header parser.c:128\n"
    "SUMMARY: AddressSanitizer: heap-buffer-overflow parser.c:128 in parse_header\n"
)

def test_run_emits_only_runtime_classes(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    docker = FakeDocker({"exec": ASAN_HEAP_WRITE, "exec_code": 1})
    v = verify_core.run(poc, vul_image="img-vul", run_cmd="./harness /tmp/poc",
                        timeout_s=30, description="heap-buffer-overflow write in parse_header",
                        docker=docker)
    assert v.failure_class in {"no_crash", "bad_format", "wrong_sink", "generic_crash"}
    assert not hasattr(v, "both_crash")
    assert v.target_likelihood in {"low", "medium", "high"}

def test_run_no_crash_is_classified(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    docker = FakeDocker({"exec": "clean exit, no sanitizer output", "exec_code": 0})
    v = verify_core.run(poc, vul_image="img-vul", run_cmd="./h /tmp/poc",
                        timeout_s=30, description="heap overflow", docker=docker)
    assert v.failure_class == "no_crash"

def test_confirm_unavailable_when_fix_missing(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    # inspect on fix image returns nonzero -> not present
    docker = FakeDocker({"inspect": "", "inspect_code": 1, "exec": ASAN_HEAP_WRITE, "exec_code": 1})
    c = verify_core.confirm(poc, vul_image="img-vul", fix_image="img-fix",
                            run_cmd="./h /tmp/poc", timeout_s=30, description="heap overflow",
                            docker=docker)
    assert c.available is False

def test_confirm_both_crash_when_fix_also_crashes(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    docker = FakeDocker({"inspect": "img-fix", "inspect_code": 0, "exec": ASAN_HEAP_WRITE, "exec_code": 1})
    c = verify_core.confirm(poc, vul_image="img-vul", fix_image="img-fix",
                            run_cmd="./h /tmp/poc", timeout_s=30, description="heap-buffer-overflow write in parse_header",
                            docker=docker)
    assert c.available is True
    assert c.both_crash is True  # crashes on fix too -> too generic
```

- [ ] **Step 3: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_verify_core.py -v`
Expected: FAIL (module missing).

- [ ] **Step 4: Implement `verify_core.py`** — port the sanitizer/crash/sink helpers; `run` maps to the four runtime classes (`no_crash` = no crash; `bad_format` = crash before parser reached / `parser_reached==False`; `wrong_sink` = crash but sink token mismatches description; `generic_crash` = crash, sink unknown/uncomparable). `target_likelihood`: `high` when sink token matches and parser reached; `medium` when crash+parser reached but sink unconfirmed; else `low`. `confirm` first `docker image inspect <fix_image>` (via injected runner); if nonzero → `available=False`; else run the poc on both images and set `both_crash = vul_crashes and fix_crashes`, `post_patch_crash = fix_crashes`, `target_match = vul_crashes and not fix_crashes and sink matches`.

- [ ] **Step 5: Run tests**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_verify_core.py -v`
Expected: 4 passed.

- [ ] **Step 6: Write `mcp/verify_server.py`** — an `mcp` stdio server exposing two tools, `verify.run` and `verify.confirm_if_available`, that read `vul_image`/`fix_image`/`run_cmd`/`timeout_s`/`description` from a config file written by the runner (Task 7) into the run dir, take a `candidate_path` arg, call `verify_core`, and return the verdict as JSON. (Server wiring is exercised in Task 10's integration test; no unit test here.)

- [ ] **Step 7: Commit**

```bash
git add src/memonaemo/verify_core.py mcp/verify_server.py tests/test_verify_core.py
git commit -m "feat: 2-tier verify (vul-only runtime diagnosis + vul+fix confirm) with signal split"
```

---

### Task 6: memory MCP server with tool-name scope boundaries

**Files:**
- Create: `mcp/memory_server.py`
- Create: `src/memonaemo/memory_api.py` (pure functions the server calls)
- Create: `tests/test_memory_scope.py`

**Interfaces:**
- Produces these MCP tools (D3 — tool name IS the scope):
  - `memory.search_okf_for_generate(query_keys: dict) -> {results: [compact_record...]}` (generate scope: OKF examples + procedural policy).
  - `memory.get_repair_policy(failure_class, verifier_signal, input_format?, harness_convention?, vuln_class?) -> {policy: compact_record | null}` (generate scope; compact record only).
  - `memory.get_discriminator_evidence(candidate_id) -> {verifier_summary, candidate_metadata}` — verifier summaries + candidate metadata ONLY; raises/returns a denial for any OKF/causal/generate field. (Defined; not used by v1 main loop — D10.)
  - `memory.record_proposal(payload) -> {proposal_path}` — writes a dry-run proposal file under the run dir; NEVER writes to `memory_store/okf/`.
  - `memory.scope_check(memory_class, tool) -> {visible: bool}`.
- `memory_api` functions are pure (take `store_dir`, `stats`, query) so they can be unit-tested without MCP.

- [ ] **Step 1: Write failing scope tests** (against `memory_api`, the pure layer)

`tests/test_memory_scope.py`:
```python
from pathlib import Path
from memonaemo import memory_api, stats

STORE = Path(__file__).resolve().parents[1] / "memory_store"

def test_repair_policy_returns_compact_only(tmp_path):
    st = stats.Stats.load(tmp_path / "s.jsonl")
    out = memory_api.get_repair_policy(STORE, st, failure_class="bad_format",
                                       verifier_signal="parser_not_reached")
    if out["policy"] is not None:
        assert set(out["policy"]) <= {"name", "policy", "procedure", "negative_memory", "evidence_level"}

def test_discriminator_evidence_denies_generate_fields():
    # The discriminator surface must never expose OKF/causal/policy content.
    ev = memory_api.get_discriminator_evidence(
        candidate_meta={"id": "c1", "crash_type": "heap-buffer-overflow"},
        verifier_summary={"failure_class": "generic_crash"},
    )
    flat = str(ev).lower()
    assert "policy" not in ev and "okf" not in flat and "procedure" not in flat

def test_scope_check_blocks_causal_policy_for_discriminator():
    assert memory_api.scope_check("causal_policy", "memory.get_discriminator_evidence")["visible"] is False
    assert memory_api.scope_check("causal_policy", "memory.get_repair_policy")["visible"] is True

def test_record_proposal_never_writes_okf(tmp_path):
    p = memory_api.record_proposal(run_dir=tmp_path, payload={"failure_class": "bad_format"})
    written = Path(p["proposal_path"])
    assert written.exists()
    assert "okf" not in str(written.resolve()).split("memory_store")[-1] if "memory_store" in str(written.resolve()) else True
    # Hard rule: nothing created under memory_store/okf
    assert not any("okf" in str(x) for x in tmp_path.rglob("*") if "memory_store" in str(x))
```

- [ ] **Step 2: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_memory_scope.py -v`
Expected: FAIL (module missing).

- [ ] **Step 3: Implement `memory_api.py`** — `search_okf_for_generate` and `get_repair_policy` use `okf.load_policies` + `okf.rank` + `okf.compact_record`. `get_discriminator_evidence` takes only `candidate_meta` + `verifier_summary` and returns exactly `{verifier_summary, candidate_metadata}` (no OKF access path exists in this function). `scope_check` consults a constant `VISIBILITY = {"causal_policy": {"memory.get_repair_policy", "memory.search_okf_for_generate"}, "okf_example": {...}, "verifier_summary": {"memory.get_discriminator_evidence", ...}}`. `record_proposal` writes JSON under `run_dir/proposals/`.

- [ ] **Step 4: Run tests**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_memory_scope.py -v`
Expected: 4 passed.

- [ ] **Step 5: Write `mcp/memory_server.py`** — stdio MCP server registering the five tools; it loads `store_dir` and the stats path from env/config set by the runner. The server process is launched with NO filesystem tools and is the only reader of `memory_store/` (D9). Integration-exercised in Task 10.

- [ ] **Step 6: Commit**

```bash
git add src/memonaemo/memory_api.py mcp/memory_server.py tests/test_memory_scope.py
git commit -m "feat: memory MCP with tool-name scope boundaries + compact repair records"
```

---

### Task 7: specialist MCP server (GPT-5.5 advisor)

**Files:**
- Create: `mcp/specialist_server.py`
- Create: `src/memonaemo/specialist_core.py`
- Create: `tests/test_specialist_core.py`

**Interfaces:**
- Produces:
  - `specialist_core.advise(kind: str, diagnosis: dict, repair_policy: dict | None, *, client=None, model: str) -> {strategy: str}` where `kind` in `{rethink_reachability, relocalize_sink, escape_basin, diversify_family, review_consolidation}`. Builds a redacted prompt (diagnosis + compact repair policy only — same scope hygiene as the agent), calls the OpenAI client, returns the strategy text. The specialist NEVER writes memory or submits.
  - `specialist_core.resolve_model(client) -> str`: returns the GPT-5.5 model id by querying `client.models.list()` and matching `gpt-5.5*` / the documented id; falls back to env `MEMONAEMO_SPECIALIST_MODEL`.
- MCP tools `specialist.rethink_reachability`, `specialist.relocalize_sink`, `specialist.escape_basin`, `specialist.diversify_family`, `specialist.review_consolidation` each call `advise` with the matching `kind`.

- [ ] **Step 1: Write failing tests** (inject a fake OpenAI client)

`tests/test_specialist_core.py`:
```python
from memonaemo import specialist_core

class FakeResp:
    def __init__(self, text): self.choices = [type("C", (), {"message": type("M", (), {"content": text})()})()]

class FakeClient:
    def __init__(self): self.captured = None
    class chat:
        pass
    def __init__(self):
        self.captured = None
        outer = self
        class _Completions:
            def create(self, **kw):
                outer.captured = kw
                return FakeResp("redesign reachability: rebuild magic + checksum gate first")
        class _Chat:
            completions = _Completions()
        self.chat = _Chat()

def test_advise_returns_strategy_and_redacts():
    c = FakeClient()
    out = specialist_core.advise(
        "rethink_reachability",
        diagnosis={"failure_class": "no_crash", "task_id": "arvo:12345"},  # task_id must be stripped
        repair_policy={"name": "no-crash-reachability", "procedure": "..."},
        client=c, model="gpt-5.5",
    )
    assert "strategy" in out and out["strategy"]
    prompt_text = str(c.captured)
    assert "arvo:12345" not in prompt_text  # redacted before leaving the box

def test_unknown_kind_rejected():
    import pytest
    with pytest.raises(ValueError):
        specialist_core.advise("hack_the_planet", diagnosis={}, repair_policy=None,
                               client=FakeClient(), model="gpt-5.5")
```

- [ ] **Step 2: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_specialist_core.py -v`
Expected: FAIL (module missing).

- [ ] **Step 3: Implement `specialist_core.py`** — validate `kind` against the allowed set; build the prompt from `task_card.redact_for_promotion(json.dumps(diagnosis))` + the compact repair policy; call `client.chat.completions.create(model=model, messages=[...])`; return `{"strategy": resp.choices[0].message.content}`. Implement `resolve_model` per the interface (query models, env fallback).

- [ ] **Step 4: Run tests**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_specialist_core.py -v`
Expected: 2 passed.

- [ ] **Step 5: Write `mcp/specialist_server.py`** — stdio MCP server; constructs the OpenAI client from `OPENAI_API_KEY`, resolves the model once at startup, registers the five tools.

- [ ] **Step 6: Commit**

```bash
git add src/memonaemo/specialist_core.py mcp/specialist_server.py tests/test_specialist_core.py
git commit -m "feat: GPT-5.5 specialist MCP advisor (redacted input, no memory/submit access)"
```

---

### Task 8: agent_driver — Agent SDK wiring + filesystem isolation (D9)

**Files:**
- Create: `src/memonaemo/agent_driver.py`
- Create: `prompts/system.md`, `prompts/kickoff.md`
- Create: `tests/test_agent_options.py`
- Reference: Agent SDK Python reference — fetch `https://platform.claude.com/docs/en/api/agent-sdk/python` (or dispatch the `claude-code-guide` agent) to confirm the exact `ClaudeAgentOptions` field names for `allowed_tools`, `cwd`, `mcp_servers`, `system_prompt`, and skills/setting sources before writing the option builder.

**Interfaces:**
- Produces:
  - `agent_driver.build_options(run_dir, skills_dir, mcp_servers: dict, model="claude-opus-4-8") -> ClaudeAgentOptions` that (a) sets `cwd=run_dir`, (b) restricts filesystem tools to `run_dir` + `skills_dir` and EXCLUDES any path under `memory_store/` (D9), (c) registers the three MCP servers, (d) loads `prompts/system.md` as the system prompt.
  - `agent_driver.solve(card, options) -> AgentResult` (async) that runs the agent loop to completion and returns `{candidate_path, transcript_path, stop_reason, cost}`.
- The system prompt encodes the tool-scope protocol (which `memory.*`/`verify.*`/`specialist.*` tool to use when) and the recon→generate flow — this is PROMPTING, not Python policy.

- [ ] **Step 1: Confirm the Agent SDK option API** by fetching the Python Agent SDK reference (above). Record the exact field names used below.

- [ ] **Step 2: Write `prompts/system.md`** — memory-first, single-agent, verification-first. Must instruct: never assume a crash is a target match (call `verify.run`, read `failure_class`); on hard failure call the matching `specialist.*`; query `memory.get_repair_policy` keyed by `failure_class × verifier_signal`; OKF is available ONLY via `memory.*` tools (you cannot read `memory_store/`); run exactly one final submission is the runner's job, not yours.

- [ ] **Step 3: Write the failing options test**

`tests/test_agent_options.py`:
```python
from pathlib import Path
from memonaemo import agent_driver

def test_options_exclude_memory_store(tmp_path):
    run = tmp_path / "run"; run.mkdir()
    skills = tmp_path / "skills"; skills.mkdir()
    opts = agent_driver.build_options(run, skills, mcp_servers={}, model="claude-opus-4-8")
    # Whatever the SDK field is, the resolved allowed roots must not include memory_store.
    roots = agent_driver.allowed_fs_roots(opts)
    assert all("memory_store" not in str(r) for r in roots)
    assert any(str(run) in str(r) for r in roots)

def test_system_prompt_loaded(tmp_path):
    opts = agent_driver.build_options(tmp_path, tmp_path, mcp_servers={})
    assert "verify.run" in agent_driver.system_prompt_text(opts)
```

- [ ] **Step 4: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_agent_options.py -v`
Expected: FAIL (module missing).

- [ ] **Step 5: Implement `agent_driver.py`** using the confirmed SDK API. Provide the small accessor helpers `allowed_fs_roots(opts)` and `system_prompt_text(opts)` so the test asserts on real option state. `solve` uses `ClaudeSDKClient`/`query` per the reference.

- [ ] **Step 6: Run tests**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_agent_options.py -v`
Expected: 2 passed.

- [ ] **Step 7: Commit**

```bash
git add src/memonaemo/agent_driver.py prompts/system.md prompts/kickoff.md tests/test_agent_options.py
git commit -m "feat: agent_driver wires Agent SDK with memory_store filesystem isolation (D9)"
```

---

### Task 9: consolidate.py — offline, train-only, dry-run, GPT-5.5 review

**Files:**
- Create: `src/memonaemo/consolidate.py`
- Create: `tests/test_consolidate.py`
- Reference: `/home/nsd/SCHE-MA/schema/simple-memory/simple_memory/causal_distill.py`

**Interfaces:**
- Produces:
  - `consolidate.propose(result_json: dict, split: dict, *, specialist=None) -> Proposal | Refusal`. Refuses when: task is eval-split, run unsolved/unverified, PoC path missing. Builds an abstract proposal (keyed by `vuln_class × input_format × harness × failure_class`) with all forbidden fields (raw bytes, task-id, submit metadata, checksums, exact offsets) stripped via `task_card.redact_for_promotion`. Dry-run by default: returns the proposal object, writes a markdown file, but does NOT mutate `memory_store/okf/`.
  - When `specialist` is provided, calls `specialist.review_consolidation` and attaches the verdict; a non-approving verdict marks the proposal `blocked`.

- [ ] **Step 1: Read** `causal_distill.py` for its refusal rules and abstract-proposal shape; port them.

- [ ] **Step 2: Write failing tests**

`tests/test_consolidate.py`:
```python
from memonaemo import consolidate

SPLIT = {"train": ["t-train-1"], "eval": ["t-eval-1"]}

def test_refuses_eval_task():
    r = consolidate.propose({"task_id": "t-eval-1", "solved": True, "poc_path": "/x"}, SPLIT)
    assert getattr(r, "refused", False) is True

def test_refuses_unsolved():
    r = consolidate.propose({"task_id": "t-train-1", "solved": False, "poc_path": "/x"}, SPLIT)
    assert getattr(r, "refused", False) is True

def test_proposal_strips_forbidden_fields(tmp_path):
    res = {"task_id": "t-train-1", "solved": True, "verified": True,
           "poc_path": str(tmp_path / "p"), "sink_loc": "parser.c:128",
           "offset": "0x4012", "checksum": "a1b2c3d4e5", "vuln_class": "heap-buffer-overflow-write",
           "input_format": "tiff", "harness": "libfuzzer", "failure_class": "wrong_sink"}
    (tmp_path / "p").write_bytes(b"poc")
    p = consolidate.propose(res, SPLIT)
    text = p.markdown
    assert "t-train-1" not in text and "0x4012" not in text and "a1b2c3d4e5" not in text
    assert "heap-buffer-overflow-write" in text and "tiff" in text  # abstract keys kept

def test_dry_run_does_not_touch_okf(tmp_path, monkeypatch):
    # propose must never write under memory_store/okf
    res = {"task_id": "t-train-1", "solved": True, "verified": True,
           "poc_path": str(tmp_path / "p"), "vuln_class": "x", "input_format": "y",
           "harness": "z", "failure_class": "no_crash"}
    (tmp_path / "p").write_bytes(b"x")
    consolidate.propose(res, SPLIT, out_dir=tmp_path)
    assert not (tmp_path / "okf").exists()
```

- [ ] **Step 3: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_consolidate.py -v`
Expected: FAIL (module missing).

- [ ] **Step 4: Implement `consolidate.py`** per the interface; reuse `task_card.redact_for_promotion`.

- [ ] **Step 5: Run tests**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_consolidate.py -v`
Expected: 4 passed.

- [ ] **Step 6: Commit**

```bash
git add src/memonaemo/consolidate.py tests/test_consolidate.py
git commit -m "feat: offline train-only dry-run consolidation with GPT-5.5 review gate"
```

---

### Task 10: cybergym_io + run.py CLI + end-to-end fake smoke

**Files:**
- Create: `src/memonaemo/cybergym_io.py`
- Create: `runner/run.py`
- Create: `tests/test_cybergym_io.py`
- Create: `tests/test_run_smoke.py`
- Reference: `/home/nsd/SCHE-MA/schema/simple-memory/simple_memory/verifier.py` (submit parsing), `/home/nsd/SCHE-MA/scripts/run_task.py`

**Interfaces:**
- Produces:
  - `cybergym_io.parse_submit(task_dir) -> SubmitMeta` (ports the `submit.sh` parsing/redaction from simple-memory's verifier) — server URL, task_id, agent_id, checksum kept ONLY for the single official submit, never surfaced to memory.
  - `cybergym_io.images_for(task_dir) -> {vul_image, fix_image}` deriving `cybergym/oss-fuzz:<id>-vul` / `-fix` tags.
  - `cybergym_io.submit_once(candidate_path, meta) -> {target_match, both_crash, raw}` — the single official submission.
  - `runner/run.py` Typer app with subcommands `solve` (prepare card → write MCP config → launch agent → optional `verify.confirm_if_available` gate → `submit_once` → write `result.json`), `consolidate` (dry-run), `batch`.
- Consumes: Tasks 4–9.

- [ ] **Step 1: Write `cybergym_io` failing tests** (fixture submit.sh, fake docker/HTTP)

`tests/test_cybergym_io.py`:
```python
from memonaemo import cybergym_io

def test_images_for(tmp_path):
    (tmp_path / "meta.json").write_text('{"id": "42537730"}')
    imgs = cybergym_io.images_for(tmp_path)
    assert imgs["vul_image"].endswith("42537730-vul")
    assert imgs["fix_image"].endswith("42537730-fix")

def test_parse_submit_redacts_in_repr(tmp_path):
    (tmp_path / "submit.sh").write_text(
        'curl -X POST http://srv:8080/submit-vul -d \'{"task_id":"arvo:1","agent_id":"a1","checksum":"c1"}\''
    )
    meta = cybergym_io.parse_submit(tmp_path)
    # The object can hold the values, but its repr/excerpt must redact them.
    assert "arvo:1" not in repr(meta)
```

- [ ] **Step 2: Run to verify failure**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_cybergym_io.py -v`
Expected: FAIL (module missing).

- [ ] **Step 3: Implement `cybergym_io.py`** (port submit parsing; derive image tags from task metadata; `submit_once` shells the curl/submit per the parsed meta).

- [ ] **Step 4: Run cybergym_io tests** — Expected: 2 passed.

- [ ] **Step 5: Write the end-to-end fake smoke test**

`tests/test_run_smoke.py`:
```python
import subprocess, sys, json, os
from pathlib import Path

def test_solve_fake_smoke(tmp_path):
    # A fake backend + fake verifier path so no Docker/model/network is touched.
    task = tmp_path / "task"; task.mkdir()
    (task / "description.txt").write_text("heap overflow in parse, tiff input")
    (task / "meta.json").write_text('{"id": "0000-fake"}')
    run_dir = tmp_path / "run"
    env = {**os.environ, "PYTHONPATH": "src", "MEMONAEMO_FAKE": "1"}
    r = subprocess.run(
        [sys.executable, "runner/run.py", "solve", "--task-dir", str(task),
         "--run-dir", str(run_dir), "--fake"],
        capture_output=True, text=True, env=env,
    )
    assert r.returncode == 0, r.stderr
    result = json.loads((run_dir / "result.json").read_text())
    assert "failure_class" in result or "target_match" in result
    # D9 sanity: the agent transcript dir must not contain memory_store paths.
    assert not list(run_dir.rglob("memory_store"))
```

- [ ] **Step 6: Implement `runner/run.py`** with a `--fake` mode that stubs the agent loop (writes a synthetic candidate) and the verifier (returns a fixed `RuntimeVerdict`) so the smoke path runs offline. Real mode wires the three MCP servers, calls `agent_driver.solve`, runs the confirm gate, and `submit_once`.

- [ ] **Step 7: Run the smoke test**

Run: `PYTHONPATH=src .venv/bin/pytest tests/test_run_smoke.py -v`
Expected: 1 passed.

- [ ] **Step 8: Run the full suite**

Run: `PYTHONPATH=src .venv/bin/pytest -q`
Expected: all green.

- [ ] **Step 9: Commit**

```bash
git add src/memonaemo/cybergym_io.py runner/run.py tests/test_cybergym_io.py tests/test_run_smoke.py
git commit -m "feat: cybergym IO + run.py CLI with offline fake smoke (single official submit)"
```

---

### Task 11: A/B harness (memory on/off) + README

**Files:**
- Create: `src/memonaemo/ab_eval.py`
- Create: `tests/test_ab_eval.py`
- Modify: `README.md`

**Interfaces:**
- Produces: `ab_eval.run(tasks, split, *, memory_on: bool, dry_run=True) -> Report` recording per the spec: attempted, target-matched, median attempts, negative-memory hit rate, submit count (must be ≤ 1/task), cost/tokens, failure-class histogram. Refuses non-train tasks. Dry-run writes a markdown report without solving.

- [ ] **Step 1: Write failing test**

`tests/test_ab_eval.py`:
```python
from memonaemo import ab_eval

SPLIT = {"train": ["t1", "t2"], "eval": ["e1"]}

def test_refuses_eval_tasks():
    rep = ab_eval.run(["e1"], SPLIT, memory_on=True, dry_run=True)
    assert rep.refused_eval == ["e1"]

def test_dry_run_report_has_required_metrics():
    rep = ab_eval.run(["t1", "t2"], SPLIT, memory_on=True, dry_run=True)
    for k in ("attempted", "target_matched", "median_attempts", "submit_count", "failure_classes"):
        assert k in rep.metrics
```

- [ ] **Step 2: Run to verify failure** — Expected: FAIL (module missing).

- [ ] **Step 3: Implement `ab_eval.py`.**

- [ ] **Step 4: Run tests** — Expected: 2 passed.

- [ ] **Step 5: Write `README.md`** documenting: architecture (link the spec), the three MCP servers, the D9 filesystem boundary, how to run `solve` / `consolidate` / `ab-eval`, the verify signal split, and the OKF leak-audit step. State plainly that live Docker/submit integration is only claimed once a real command is captured as evidence.

- [ ] **Step 6: Run the full suite** — Run: `PYTHONPATH=src .venv/bin/pytest -q` — Expected: all green.

- [ ] **Step 7: Commit**

```bash
git add src/memonaemo/ab_eval.py tests/test_ab_eval.py README.md
git commit -m "feat: train-only A/B harness (memory on/off) + README"
```

---

## Verification (whole-plan)

After Task 11, confirm the spec's twelve sections map to tasks:
- §3 curated import → Task 2 (+ leak audit). §4 memory model / §7 retrieval → Tasks 3, 6. §5 data flow → Task 10. §6 2-tier verify → Task 5. §8 multi-model → Task 7. §9 consolidation → Task 9. §10 five bets → Tasks 3/5/6/9 collectively. §12 testing → tests in every task + Task 11.
- D9 (filesystem isolation) is asserted by tests in Task 8 and Task 10.
- D3 (tool-name scope) is asserted in Task 6. D11 (redaction altitude) in Tasks 4 and 9. Verify signal split in Task 5.

Real-environment validation (run once Docker/keys are intentionally engaged, captured as evidence, NOT part of the offline suite):
1. `runner/run.py solve` against one **train** task with real Docker + Agent SDK + `ANTHROPIC_API_KEY`/`OPENAI_API_KEY`.
2. Confirm exactly one `submit.sh` call per task in the run log.
3. Confirm the agent session cannot read `memory_store/` (grep the transcript for OKF body text that only exists in `memory_store/okf/` — it must arrive only via `memory.*` tool results).
