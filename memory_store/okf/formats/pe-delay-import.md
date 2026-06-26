---
type: format-family
title: "PE Delay Import format"
description: "Round 8 descriptive format facts for pe-delay-import."
resource: cybergym://format/pe-delay-import
tags: ["pe-delay-import", "round-8"]
okf_support: 1
---
# PE Delay Import Format

## Round 8 Factual Contract

### Schema / Invariants
- A PE delay-import candidate needs a normal DOS and PE header, an optional-header data-directory entry for delay imports, a section mapping the delay-import descriptor table, and descriptor fields for DLL-name RVA, import address table RVA, and import name table RVA. The signedness-sensitive field is an RVA that pe_rva_to_offset cannot map to a file offset.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

