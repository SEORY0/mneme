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
