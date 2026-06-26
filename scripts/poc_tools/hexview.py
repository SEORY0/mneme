#!/usr/bin/env python3
"""hexview.py — quick binary inspection for PoC construction (no ad-hoc struct heredocs).

Replaces the repeated `python3 - <<PY ... struct.unpack ... PY` pattern workers were
using to read binary structure. Three modes:

  slice    — xxd-like hex+ASCII of a byte range (offset/len).
  records  — dump fixed-stride records (base + stride + count), first bytes of each.
  offsets  — parse an OFFSET TABLE (e.g. a font loca table) into record spans and dump
             each record's first bytes. This is the font glyf/loca case directly.

All parsing helpers are pure functions (unit-tested); only `main` touches the filesystem.

Examples:
  python3 scripts/poc_tools/hexview.py slice f.bin --offset 0x2200 --len 64
  python3 scripts/poc_tools/hexview.py records f.bin --base 8768 --stride 374 --count 14 --head 20
  python3 scripts/poc_tools/hexview.py offsets f.bin --table-at 0x100 --count 15 --entry u16 --base 8768 --head 20
"""
from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path
from typing import List, Tuple


def format_hex(data: bytes, offset: int = 0, length: int | None = None, width: int = 16) -> str:
    """xxd-style hex+ASCII dump of data[offset:offset+length]."""
    end = len(data) if length is None else min(len(data), offset + length)
    out = []
    for base in range(offset, end, width):
        chunk = data[base:min(base + width, end)]
        hexpart = " ".join(f"{b:02x}" for b in chunk)
        asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        out.append(f"{base:08x}  {hexpart:<{width * 3}}  {asc}")
    return "\n".join(out)


def parse_offset_table(data: bytes, table_at: int, count: int, entry: str = "u16",
                       endian: str = ">", scale: int = 1, base: int = 0) -> List[int]:
    """Read `count` offsets from an offset table at `table_at`.

    entry ∈ {u16,u32}; offsets are multiplied by `scale` (font loca short entries are
    /2) and `base` is added. Returns the absolute offsets.
    """
    fmt = {"u16": "H", "u32": "I"}[entry]
    sz = struct.calcsize(fmt)
    offs = []
    for i in range(count):
        (v,) = struct.unpack_from(endian + fmt, data, table_at + i * sz)
        offs.append(base + v * scale)
    return offs


def record_spans(offsets: List[int], end: int | None = None) -> List[Tuple[int, int, int]]:
    """Turn a sorted offset list into (index, start, length) spans. The last record runs
    to `end` (or to the next offset if `end` is None and it is the final boundary)."""
    spans = []
    for i in range(len(offsets) - 1):
        spans.append((i, offsets[i], offsets[i + 1] - offsets[i]))
    if end is not None and offsets:
        spans.append((len(offsets) - 1, offsets[-1], end - offsets[-1]))
    return spans


def fixed_records(total_len: int, base: int, stride: int, count: int) -> List[Tuple[int, int, int]]:
    """(index, start, length) for `count` fixed-stride records starting at `base`."""
    out = []
    for i in range(count):
        start = base + i * stride
        if start >= total_len:
            break
        out.append((i, start, min(stride, total_len - start)))
    return out


def _dump_spans(data: bytes, spans: List[Tuple[int, int, int]], head: int) -> str:
    lines = []
    for idx, start, length in spans:
        h = data[start:start + head].hex()
        lines.append(f"  rec {idx:>4} off {start:>8} len {length:>6}  {h}")
    return "\n".join(lines)


def _auto_int(s: str) -> int:
    return int(s, 0)  # handles 0x.. and decimal


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)

    s = sub.add_parser("slice")
    s.add_argument("file"); s.add_argument("--offset", type=_auto_int, default=0)
    s.add_argument("--len", dest="length", type=_auto_int, default=256)

    r = sub.add_parser("records")
    r.add_argument("file"); r.add_argument("--base", type=_auto_int, required=True)
    r.add_argument("--stride", type=_auto_int, required=True)
    r.add_argument("--count", type=_auto_int, required=True)
    r.add_argument("--head", type=_auto_int, default=16)

    o = sub.add_parser("offsets")
    o.add_argument("file"); o.add_argument("--table-at", type=_auto_int, required=True)
    o.add_argument("--count", type=_auto_int, required=True)
    o.add_argument("--entry", choices=["u16", "u32"], default="u16")
    o.add_argument("--endian", choices=[">", "<"], default=">")
    o.add_argument("--scale", type=_auto_int, default=1)
    o.add_argument("--base", type=_auto_int, default=0)
    o.add_argument("--head", type=_auto_int, default=16)

    args = ap.parse_args(argv)
    data = Path(args.file).read_bytes()

    if args.mode == "slice":
        print(format_hex(data, args.offset, args.length))
    elif args.mode == "records":
        spans = fixed_records(len(data), args.base, args.stride, args.count)
        print(_dump_spans(data, spans, args.head))
    elif args.mode == "offsets":
        offs = parse_offset_table(data, args.table_at, args.count, args.entry,
                                  args.endian, args.scale, args.base)
        spans = record_spans(offs, end=offs[-1])  # last boundary = final offset
        print(f"offsets: {offs}")
        print(_dump_spans(data, spans, args.head))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
