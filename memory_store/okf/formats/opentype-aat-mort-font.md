---
type: format-family
title: "opentype-aat-mort-font format"
description: "Structure and invariants observed for opentype-aat-mort-font."
resource: "cybergym://format/opentype-aat-mort-font"
tags: ["opentype-aat-mort-font", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- AAT mort/morx inputs are complete sfnt fonts with normal table records. HarfBuzz prefers the extended AAT substitution table when present and falls back to the obsolete table only when the extended table is absent, so a mort-targeting PoC must ensure the obsolete table is the selected AAT substitution source. A mort table contains a table header, one or more chains, chain feature records, and chain subtables. A contextual subtable embeds an obsolete state table followed by a substitution-table offset field. The obsolete state table can be made sanitizable with a degenerate class/state arrangement even when the contextual subtable body omits the later substitution-table offset field.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
