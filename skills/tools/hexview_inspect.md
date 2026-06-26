---
name: hexview_inspect
description: Structured READ/inspect of an existing binary (hex slices, fixed-stride records, offset tables) without ad-hoc struct heredocs
type: tool
availability: always
required_package: ~
requires_tools: []
triggers: [understand_format, seed_inspect, offset_table, record_table, no_crash]
token_cost: low
---
<tool_skill name="hexview" availability="always">
# hexview — Inspect existing binary structure

Use this instead of writing one-off `python3 - <<PY ... struct.unpack ... PY` heredumps to
read a sample/seed's layout. `construct_format_builder` is for BUILDING; `hexview` is for
READING what is already there (a seed you will mutate, or the structure you must reproduce).

## When to use
- You extracted a seed/sample from `repo-vul` and need to see its header / record table.
- A format has an OFFSET TABLE (font `loca`, container index, archive directory) and you want
  each record's span + first bytes.
- You want a quick xxd-style slice at a specific offset while debugging a `no_crash`.

## Usage via bash tool
```bash
# hex+ASCII slice of a byte range
python3 scripts/poc_tools/hexview.py slice SAMPLE --offset 0x2200 --len 64

# fixed-stride records (base + stride + count): dump first bytes of each
python3 scripts/poc_tools/hexview.py records SAMPLE --base 8768 --stride 374 --count 14 --head 20

# OFFSET TABLE (e.g. font loca: u16 entries, /2 scale, plus glyf base) -> record spans
python3 scripts/poc_tools/hexview.py offsets SAMPLE --table-at 0x100 --count 15 \
    --entry u16 --scale 2 --base 8768 --head 20
```
`--offset/--base/--table-at` accept hex (`0x..`) or decimal. `offsets` prints the resolved
offset list, then `rec <i> off <start> len <n>  <first-bytes-hex>` per record — replacing the
manual unpack loop you would otherwise write.

## When NOT to use
- Building a new file from scratch → use `construct_format_builder`.
- A flat blob < 32 bytes → just `xxd SAMPLE` or `xxd -s OFF -l N SAMPLE`.

## Pattern (attacks no_crash)
1. Extract a real sample of the format from `repo-vul` (test/corpus dirs often ship one).
2. `hexview offsets/records` to learn the real header/table layout and gate values.
3. Copy the sample, patch the ONE field that violates the invariant (seed-mutate), re-verify.
   Seed-mutating a real sample reaches the parser far more reliably than a hand-built envelope.
</tool_skill>
