---
type: format-family
title: nbap-per-over-sctp format
description: "Round 23 descriptive structure and invariant facts for nbap-per-over-sctp."
resource: cybergym://format/nbap-per-over-sctp
tags: ["nbap-per-over-sctp", "round-23"]
okf_support: 1
train_only: true
---
# Nbap Per Over Sctp Format

## Round 23 Factual Contract

### Schema / Invariants
- NBAP is an ASN.1 PER protocol. The dissector registers a root NBAP dissector, procedure-specific dissector tables, and many generated IE/extension handlers. The vulnerable class involves generated code indexing fixed logical-channel mapping arrays from PER-decoded item counts or identifiers.

### Harness Links
- [[fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
