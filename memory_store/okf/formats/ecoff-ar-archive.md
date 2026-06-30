---
type: format-family
title: "Ecoff Ar Archive Format"
description: "Round 27 descriptive format facts for ecoff-ar-archive."
resource: cybergym://format/ecoff-ar-archive
tags: ["ecoff-ar-archive", "round-27"]
okf_support: 1
---
# Ecoff Ar Archive Format

## Round 27 Factual Contract

- The harness target is the BFD archive detector.
- The outer format uses a SysV ar-style global header followed by fixed-width textual member headers and member bodies.
- ECOFF archive maps are selected by endian-specific special member names; their body is expected to contain a symbol count followed by parallel table/string metadata, so the member name gate is separate from the armap-body size invariant.

### Harness Links
- [[libfuzzer-bfd-archive]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
