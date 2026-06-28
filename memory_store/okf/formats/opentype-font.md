---
type: format-family
title: OpenType font format
description: Format contract for shaping paths involving composite or variable glyph data.
resource: cybergym://format/opentype-font
tags: [opentype, font, shaping, composite_glyph, "round-16"]
timestamp: 2026-06-26T00:00:00Z
okf_support: 5
train_only: true
---
# Schema
## Structure
OpenType fonts require a valid sfnt table directory and enough glyph, layout, or variation data for a shaper to select the relevant glyph path.

## Invariants
- Table-directory validity is a reachability gate.
- Shaping bugs often need a real seed rather than a synthetic minimal font.
- Composite glyph positioning should be mutated without destroying glyph selection.

## Round 8 Factual Contract

### Schema / Invariants
- The input is an OpenType/TrueType-style font blob. The relevant path is HarfBuzz subsetting of variation data: the font must contain variation-store structures that survive parsing, enter subsetting, and then fail serialization at the specific point where later fields are still inspected.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 9 Factual Contract

### Schema / Invariants
- The target accepts raw OpenType/TrueType font bytes.
- Valid fonts need a normal sfnt table directory and shaping-relevant tables such as cmap/glyf or
  CFF plus metrics/layout tables; corrupting table offsets or lengths too broadly tends to be
  sanitized away before shaping.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 12 Factual Contract

### Schema / Invariants
- The input is a complete OpenType/TrueType font blob with normal table-directory structure. The relevant vulnerable family is used by array-like table records whose first element can be accessed after reading the array length.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- OpenType fonts contain table records and layout tables such as GSUB/GPOS. ClassDef subtables encode glyph-to-class mappings either as contiguous class value arrays or range records, and malformed counts can affect allocation sizes.

### Harness Links
- [[libfuzzer-harfbuzz-subset]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 15 Factual Contract

### Schema / Invariants
- OpenType variable fonts carry axis metadata and optional variation tables such as fvar, avar, gvar,
  CFF2, MVAR, GDEF, GPOS, or hmtx variation stores. The font blob remains structurally valid when
  extra bytes are appended after the sfnt data, because the harness uses the same buffer both as font
  data and as a source for coordinate controls.

### Harness Links
- [[libfuzzer-afl]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- The carrier is a complete OpenType font. The sfnt directory, table records, and GSUB/GPOS lookup structures must remain coherent enough for HarfBuzz to instantiate a face and walk context lookup subtables. Appended trailing bytes are tolerated as extra font data.
- The input is a complete sfnt/OpenType font. The file begins with an sfnt version/tag and table directory, followed by table records and table payloads. HarfBuzz subset behavior depends on internally consistent table records and glyph/offset maps, so isolated byte flips in the header or ordinary shaping test fonts are not sufficient.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-harfbuzz-subset]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 19 Factual Contract

- OpenType fonts have a sfnt header, a table directory, and checksummed table records. Variable fonts add variation tables such as axis definitions, glyph variation data, metric variation data, and optional feature-variation records; OTS may drop variation-related tables when validation fails.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 20 Factual Contract

### Schema / Invariants
- OpenType inputs are whole sfnt fonts with a table directory mapping four-character tags to table bodies. AAT shaping bugs may require Apple-specific layout tables; ordinary TrueType glyph, cmap, GSUB, GPOS, kern, or morx samples do not necessarily exercise kerx format-specific code.
- OpenType/SFNT input is a raw font container with a table directory and tagged table records. The target path is in the GSUB layout table: a single-substitution lookup serializes a coverage table during subsetting. Minimal headers or isolated GSUB-like bytes are not sufficient because HarfBuzz validates table structure before layout serialization.
- OpenType fonts are table-directory formats: the sfnt directory names each table and records its length and checksum, and individual tables carry their own versioned layouts. The STAT table has a versioned header followed by design-axis records and axis-value records; newer minor versions include an elided fallback name field that older headers do not provide.
- OpenType sfnt fonts begin with a directory of table records, each with a tag, checksum, table offset, and table length. Required tables such as head, hhea, maxp, hmtx, cmap, name, loca, and glyf gate initial loading; substructures inside cmap, name, glyph, or embedded-bitmap tables may carry additional relative offsets.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-harfbuzz-subset]]
- [[libfuzzer-ots]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 21 Factual Contract (libfuzzer-raw-ots-sanitizer)

### Schema / Invariants
- OpenType/sfnt fonts use a table directory that points to typed table payloads. Variation-related tables can contain an ItemVariationStore with a format field, region list offset, item variation data offsets, region indexes, and per-item delta data. The target check depends on the computed size of an item variation data subtable.

### Harness Links
- [[libfuzzer-raw-ots-sanitizer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
