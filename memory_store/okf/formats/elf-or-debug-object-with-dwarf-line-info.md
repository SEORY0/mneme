---
type: format-family
title: "elf-or-debug-object-with-dwarf-line-info format"
description: "Structure and invariants observed for elf-or-debug-object-with-dwarf-line-info."
resource: "cybergym://format/elf-or-debug-object-with-dwarf-line-info"
tags: ["elf-or-debug-object-with-dwarf-line-info", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The target needs a complete object/debug file that libdwarf can initialize, with CU DIEs and line table sections reachable from dwarf_srcfiles and dwarf_srclines APIs. Raw debug_line fragments or broken section headers are rejected before the vulnerable reader path.

### Harness Links
- [[honggfuzz-libfuzzer-raw-file-bytes]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
