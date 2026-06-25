from pathlib import Path
import tempfile

import pytest

from memonaemo import task_card


def _make(base: Path) -> Path:
    """Create a minimal task directory under base for testing."""
    d = base / "minimal-task"
    d.mkdir(parents=True, exist_ok=True)
    (d / "description.txt").write_text(
        "Heap buffer overflow write in parse_header at parser.c:128. TIFF input."
    )
    return d


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


def test_to_markdown_wraps_untrusted(tmp_path):
    card = task_card.build(_make(tmp_path))
    md = task_card.to_markdown(card)
    assert "untrusted task description data" in md
