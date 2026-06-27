---
type: format-family
title: "samba-ndr-drsblobs format"
description: "Structure and reachability facts for samba-ndr-drsblobs."
resource: cybergym://format/samba-ndr-drsblobs
tags: ["samba-ndr-drsblobs"]
okf_support: 1
---
# Samba Ndr Drsblobs Format

## Round 9 Factual Contract

### Schema / Invariants
- The input starts with a small little-endian NDR fuzzer selector header: flags choose
  struct/in/out/NDR64 mode and a public-struct number chooses the drsblobs structure.
- The remaining bytes are NDR stub data.
- The schedule structure contains a size, constant-valued fields, schedule header records, and
  schedule slot records whose count is controlled by the schedule count relation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
