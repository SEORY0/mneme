---
type: format-family
title: "Ndpi Custom Protocol Rules format"
description: "Descriptive contract facts for ndpi-custom-protocol-rules."
resource: "cybergym://format/ndpi-custom-protocol-rules"
tags: ["ndpi-custom-protocol-rules", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- nDPI custom protocol files are line-oriented rules.
- Risk-mask rules use an attribute name, an IP or host value, optional CIDR-style suffixes, and a mask value.
- IP rules dispatch into IPv4/IPv6 parsing before adding prefixes to a patricia tree.

### Harness Links
- [[libfuzzer-raw-rules-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
