---
type: format-family
title: bfd-archive-or-object format
description: Structure, build skeleton, and bug-prone areas of the bfd-archive-or-object input format.
resource: cybergym://format/bfd-archive-or-object
tags: [bfd-archive-or-object, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The useful carrier family is BFD file bytes. Unix ar archives require a global magic, fixed-width member headers, declared member sizes, and even-byte padding. BFD may also auto-probe object signatures inside members, including DOS, COFF, and XCOFF-like envelopes, but malformed top-level wrappers are discarded cleanly.

### Harness Links
- [[libfuzzer-tempfile-bfd]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
