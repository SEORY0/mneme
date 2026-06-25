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
        __import__("yaml")
        return True
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
            name=f.stem,
            body=body,
            match_keys=keys,
            allowed_scopes=list(meta.get("allowed_scopes", ["generate"])),
            evidence_level=str(meta.get("evidence_level", meta.get("confidence", "low"))),
            train_only=bool(meta.get("train_only", True)),
            meta=meta,
        ))
    return policies


def matches(p: Policy, query: dict) -> bool:
    wanted = {str(v) for v in query.values() if v}
    return bool(wanted & set(p.match_keys)) or any(
        str(query.get(k)) == str(p.meta.get(k))
        for k in ("failure_class", "verifier_signal", "input_format", "harness_convention", "vuln_class")
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
