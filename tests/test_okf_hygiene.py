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
