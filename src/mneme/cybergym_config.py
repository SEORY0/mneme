"""
cybergym_config: tiny .env loader + Config dataclass for the real CyberGym harness.

We do NOT assume python-dotenv is installed. ``load_config()`` reads the repo-root
``.env`` (KEY=VALUE lines) into ``os.environ`` for any keys not already set, then
builds a :class:`Config` from the environment with the documented defaults.

Keys consumed (env_prefix CYBERGYM_, plus the model API keys):
  CYBERGYM_SERVER_URL    default http://127.0.0.1:8666
  CYBERGYM_DATA_DIR      default /data/cybergym_data/data
  CYBERGYM_MASK_MAP      default <repo>/external/cybergym/mask_map.json
  CYBERGYM_PYTHON        default sys.executable (interpreter that can import cybergym)
  CYBERGYM_SRC           default <repo>/external/cybergym/src
  CYBERGYM_API_KEY       default cybergym's hardcoded server default key
  ANTHROPIC_API_KEY / OPENAI_API_KEY are loaded into os.environ but not stored here.
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path

# Repo root = two levels up from this file (src/mneme/cybergym_config.py).
_REPO_ROOT = Path(__file__).resolve().parents[2]

# cybergym's hardcoded server default (see cybergym.server.types.ServerConfig.api_key).
# The local server was started without a CYBERGYM_API_KEY override, so this is what
# /verify-agent-pocs and /query-poc expect.
_DEFAULT_CYBERGYM_API_KEY = "cybergym-030a0cd7-5908-4862-8ab9-91f2bfc7b56d"
_DEFAULT_SERVER_URL = "http://127.0.0.1:8666"
_DEFAULT_DATA_DIR = "/data/cybergym_data/data"


def _parse_env_file(text: str) -> dict[str, str]:
    """Parse simple KEY=VALUE .env lines. Ignores blanks, comments, malformed lines.

    Strips surrounding single/double quotes and an optional leading ``export``.
    """
    out: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if (len(value) >= 2) and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        if key:
            out[key] = value
    return out


def load_dotenv(env_path: Path | None = None) -> dict[str, str]:
    """Load .env into os.environ for keys that are absent or empty.

    A pre-existing EMPTY env var (common shell-profile pollution, e.g.
    ``export ANTHROPIC_API_KEY=``) blocks population, so we treat empty values as
    absent and let the .env value win. A real (non-empty) env var still overrides .env.

    Returns the parsed dict (regardless of what was applied).
    """
    if env_path is None:
        env_path = _REPO_ROOT / ".env"
    if not env_path.is_file():
        return {}
    parsed = _parse_env_file(env_path.read_text(encoding="utf-8"))
    for key, value in parsed.items():
        if not os.environ.get(key):  # absent or empty
            os.environ[key] = value
    return parsed


@dataclass
class Config:
    """Resolved CyberGym harness configuration.

    Holds non-secret harness paths plus the cybergym API key used for the private
    verify/query endpoints. The model API keys (ANTHROPIC/OPENAI) are loaded into
    os.environ by ``load_config`` but intentionally not stored on this object.
    """

    server_url: str
    data_dir: str
    mask_map: str
    cybergym_python: str
    cybergym_src: str
    cybergym_api_key: str

    def __repr__(self) -> str:
        # Redact the api key in repr/str so the object is log-safe.
        return (
            f"Config(server_url={self.server_url!r}, data_dir={self.data_dir!r}, "
            f"mask_map={self.mask_map!r}, cybergym_python={self.cybergym_python!r}, "
            f"cybergym_src={self.cybergym_src!r}, cybergym_api_key='[redacted]')"
        )

    __str__ = __repr__


def load_config(env_path: Path | None = None) -> Config:
    """Load .env (if present) then build a Config from the environment + defaults."""
    load_dotenv(env_path)

    default_mask_map = str(_REPO_ROOT / "external" / "cybergym" / "mask_map.json")
    default_src = str(_REPO_ROOT / "external" / "cybergym" / "src")

    return Config(
        server_url=os.environ.get("CYBERGYM_SERVER_URL") or _DEFAULT_SERVER_URL,
        data_dir=os.environ.get("CYBERGYM_DATA_DIR") or _DEFAULT_DATA_DIR,
        mask_map=os.environ.get("CYBERGYM_MASK_MAP") or default_mask_map,
        cybergym_python=os.environ.get("CYBERGYM_PYTHON") or sys.executable,
        cybergym_src=os.environ.get("CYBERGYM_SRC") or default_src,
        cybergym_api_key=os.environ.get("CYBERGYM_API_KEY") or _DEFAULT_CYBERGYM_API_KEY,
    )
