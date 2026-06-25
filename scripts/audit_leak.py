"""Scan a directory tree of markdown for task-id / submit-metadata leakage."""
import re, sys
from pathlib import Path

PATTERNS = [
    r"arvo:\d+",
    r"\b\d{8,}-(?:vul|fix)\b",
    r"submit-vul",
    r"\bchecksum\b\s*[:=]\s*[0-9a-f]{8,}",
]

def main(root: str = None) -> int:
    if root is None:
        # Default: scan both memory_store/okf and skills
        roots = ["memory_store/okf", "skills"]
    else:
        # If explicit root provided, use only that path
        roots = [root]

    rx = [re.compile(p, re.IGNORECASE) for p in PATTERNS]
    bad = []
    for root_path in roots:
        for f in Path(root_path).rglob("*.md"):
            t = f.read_text(encoding="utf-8")
            for r in rx:
                if r.search(t):
                    bad.append(f"{f}: {r.pattern}")
    for b in bad:
        print(b)
    return 1 if bad else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else None))
