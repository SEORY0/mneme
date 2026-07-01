---
type: format-family
title: "uri format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/uri"
tags: ["uri", "round-35"]
okf_support: 1
train_only: true
---
# uri Format

## Round 35 Factual Contract
### Schema / Invariants
- GLib URI parsing handles absolute URIs with scheme, authority, optional bracketed IPv6 literals, optional scope identifiers inside the brackets, path, query, and fragment. For scoped IPv6 hosts, the parser recognizes raw scope syntax and encoded scope separators, rejects multiple percent markers in the bracketed host, and serializes successful parses through the URI object model.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
