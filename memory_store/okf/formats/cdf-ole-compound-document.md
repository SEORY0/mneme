---
type: format-family
title: "cdf-ole-compound-document format"
description: "Structure and invariants observed for cdf-ole-compound-document."
resource: "cybergym://format/cdf-ole-compound-document"
tags: ["cdf-ole-compound-document", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- CDF/OLE parsing starts from a fixed header with magic, byte order, sector-size powers, master SAT entries, directory-chain roots, and optional short-sector allocation metadata. Long-sector reads compute a byte position from the sector size and signed sector id. Directory entries name root storage and user streams; small user streams are read through the short-sector path using the root storage stream and SSAT chain.

### Harness Links
- [[libfuzzer-libmagic-magic-buffer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
