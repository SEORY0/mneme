---
type: format-family
title: bfd-archive-containing-truncated-msdos-member format
description: Structure and reachability facts for bfd-archive-containing-truncated-msdos-member inputs.
tags: [bfd-archive-containing-truncated-msdos-member]
okf_support: 0
---
# BFD Archive Containing Truncated MSDOS Member Format

## Round 10 Factual Contract

### Schema / Invariants
- The BFD archive path expects the global archive magic, fixed-width member headers, member sizes, and even-byte member padding. The MS-DOS object probe begins with a DOS executable signature and then expects enough header bytes to validate follow-on executable metadata.

### Harness Links
- [[libfuzzer-tempfile-bfd]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
