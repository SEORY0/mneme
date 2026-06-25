"""
cybergym_io: task directory parsing, image tag derivation, and single official submit.

Design:
- parse_submit(task_dir) -> SubmitMeta
  Ports the _SERVER_RE/_FIELD_RE parsing from SCHE-MA's simple-memory verifier.
  The SubmitMeta object holds the real values internally but its __repr__ and
  __str__ always emit [redacted-submit-metadata] in place of sensitive tokens.

- images_for(task_dir) -> {"vul_image": ..., "fix_image": ...}
  Reads meta.json {"id": "..."} and derives cybergym/oss-fuzz:<id>-vul / -fix.

- submit_once(candidate_path, meta) -> {"target_match": ..., "both_crash": ..., "raw": ...}
  Single official HTTP submission.  Uses the parsed server URL, task_id, agent_id,
  checksum.  In --fake / MEMONAEMO_FAKE mode this is never called.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Final

# ---------------------------------------------------------------------------
# Regex constants ported from SCHE-MA simple-memory verifier.py
# ---------------------------------------------------------------------------
_SERVER_RE: Final = re.compile(r"curl\s+-X\s+POST\s+(?P<url>\S+)/submit-vul")
_FIELD_RE: Final = re.compile(r'"(?P<key>task_id|agent_id|checksum)"\s*:\s*"(?P<value>[^"]+)"')
_REDACTED: Final = "[redacted-submit-metadata]"


# ---------------------------------------------------------------------------
# SubmitMeta — holds sensitive values but redacts them in repr/str
# ---------------------------------------------------------------------------

@dataclass
class SubmitMeta:
    """Parsed submit.sh metadata.

    Internal fields hold real values for the single official submit only.
    __repr__ and __str__ ALWAYS redact every sensitive token so the object
    can be logged, stored, or surfaced to the agent transcript safely.
    """
    task_id: str
    agent_id: str
    checksum: str
    server_url: str

    # --- redaction helpers ---

    def _tokens(self) -> tuple[str, ...]:
        return (self.task_id, self.agent_id, self.checksum, self.server_url)

    def _redact(self, text: str) -> str:
        for tok in self._tokens():
            if tok:
                text = text.replace(tok, _REDACTED)
        return text

    def __repr__(self) -> str:
        return (
            f"SubmitMeta(task_id={_REDACTED!r}, agent_id={_REDACTED!r}, "
            f"checksum={_REDACTED!r}, server_url={_REDACTED!r})"
        )

    def __str__(self) -> str:
        return self.__repr__()

    def excerpt(self) -> str:
        """Return a redacted excerpt suitable for logging."""
        return _REDACTED


@dataclass
class SubmitMetaError:
    """Returned when submit.sh is missing or incomplete."""
    message: str
    redaction_tokens: tuple[str, ...]

    def __repr__(self) -> str:
        # Redact any partial tokens that leaked into the message
        msg = self.message
        for tok in self.redaction_tokens:
            if tok:
                msg = msg.replace(tok, _REDACTED)
        return f"SubmitMetaError(message={msg!r})"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def parse_submit(task_dir: Path | str) -> SubmitMeta | SubmitMetaError:
    """Parse submit.sh from task_dir and return a SubmitMeta (or SubmitMetaError).

    Ported from SCHE-MA simple-memory verifier._parse_submit_metadata.
    The returned SubmitMeta redacts all sensitive tokens in repr/str.
    """
    task_dir = Path(task_dir)
    path = task_dir / "submit.sh"

    if not path.is_file():
        return SubmitMetaError("submit metadata incomplete: missing submit.sh", ())

    text = path.read_text()
    fields = {
        match.group("key"): match.group("value")
        for match in _FIELD_RE.finditer(text)
    }
    server = _SERVER_RE.search(text)
    server_url = server.group("url") if server else ""

    missing = tuple(
        name
        for name in ("task_id", "agent_id", "checksum", "server_url")
        if not (server_url if name == "server_url" else fields.get(name))
    )
    tokens = tuple(value for value in (*fields.values(), server_url) if value)

    if missing:
        return SubmitMetaError(
            f"submit metadata incomplete: missing {', '.join(missing)}",
            tokens,
        )

    return SubmitMeta(
        task_id=fields["task_id"],
        agent_id=fields["agent_id"],
        checksum=fields["checksum"],
        server_url=server_url,
    )


def images_for(task_dir: Path | str) -> dict[str, str]:
    """Derive cybergym/oss-fuzz image tags from task metadata.

    Reads meta.json {"id": "<numeric-oss-fuzz-id>"} and returns:
      {"vul_image": "cybergym/oss-fuzz:<id>-vul",
       "fix_image": "cybergym/oss-fuzz:<id>-fix"}

    Does NOT require docker to be present — purely string derivation.
    """
    task_dir = Path(task_dir)
    meta_path = task_dir / "meta.json"
    if not meta_path.is_file():
        raise FileNotFoundError(f"meta.json not found in {task_dir}")

    meta = json.loads(meta_path.read_text())
    task_id = str(meta["id"])

    return {
        "vul_image": f"cybergym/oss-fuzz:{task_id}-vul",
        "fix_image": f"cybergym/oss-fuzz:{task_id}-fix",
    }


def submit_once(
    candidate_path: Path | str,
    meta: SubmitMeta,
) -> dict:
    """Single official submission via curl.

    Shells out to curl exactly once — mirrors the submit.sh pattern.
    Returns {"target_match": bool, "both_crash": bool, "raw": str}.

    Only call this in real (non-fake) mode.  In --fake / MEMONAEMO_FAKE mode
    the caller must NOT call this function.
    """
    candidate_path = Path(candidate_path)
    url = f"{meta.server_url}/submit-vul"

    result = subprocess.run(
        [
            "curl", "-s", "-X", "POST", url,
            "-F", f"file=@{candidate_path}",
            "-F", f"task_id={meta.task_id}",
            "-F", f"agent_id={meta.agent_id}",
            "-F", f"checksum={meta.checksum}",
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    raw = result.stdout + result.stderr
    try:
        data = json.loads(result.stdout)
        return {
            "target_match": bool(data.get("target_match", False)),
            "both_crash": bool(data.get("both_crash", False)),
            "raw": raw,
        }
    except (json.JSONDecodeError, ValueError):
        return {"target_match": False, "both_crash": False, "raw": raw}
