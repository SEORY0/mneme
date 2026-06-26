"""Offline tests for scripts/poc_tools/hexview.py (pure parsing helpers)."""
import struct
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "poc_tools"))
import hexview as H  # noqa: E402


def test_format_hex_slice():
    data = bytes(range(32))
    out = H.format_hex(data, offset=16, length=8)
    # one row starting at 0x10, bytes 10..17
    assert out.startswith("00000010  10 11 12 13 14 15 16 17")


def test_parse_offset_table_u16_scaled():
    # font-loca-style: u16 entries, /2 means scale=2, plus a base
    tbl = struct.pack(">4H", 0, 115, 124, 442)  # offsets/2
    offs = H.parse_offset_table(tbl, table_at=0, count=4, entry="u16", scale=2, base=8768)
    assert offs == [8768, 8768 + 230, 8768 + 248, 8768 + 884]


def test_record_spans_lengths():
    offs = [8768, 8998, 9246, 10130]
    spans = H.record_spans(offs, end=offs[-1])
    # (idx, start, length) — last span has zero length at the final boundary
    assert spans[0] == (0, 8768, 230)
    assert spans[1] == (1, 8998, 248)
    assert spans[2] == (2, 9246, 884)


def test_fixed_records_clips_to_eof():
    recs = H.fixed_records(total_len=100, base=80, stride=30, count=5)
    # base 80 -> [80,30 clipped to 20]; next start 110 >= 100 -> stop
    assert recs == [(0, 80, 20)]


def test_fixed_records_full():
    recs = H.fixed_records(total_len=1000, base=0, stride=100, count=3)
    assert recs == [(0, 0, 100), (1, 100, 100), (2, 200, 100)]
