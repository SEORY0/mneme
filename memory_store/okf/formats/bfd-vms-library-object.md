---
type: format-family
title: "BFD VMS Library Object Format"
description: "Round 27 descriptive format facts for bfd-vms-library-object."
resource: cybergym://format/bfd-vms-library-object
tags: ["bfd-vms-library-object", "round-27"]
okf_support: 1
---
# BFD VMS Library Object Format

## Round 27 Factual Contract

- A VMS library has a fixed-size library header with a library type, a sanity id, a major version, module and symbol counts, and index descriptors.
- Alpha object libraries require the Alpha object or Alpha share-image library type, the Alpha library major version, and two ASCII variable-length indexes.
- VMS object modules are record-based: object records carry a record type and repeated size information, an EMH/MHD-style record starts module metadata, and an EEOM-style record terminates the module.

### Harness Links
- [[libfuzzer-bfd]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
