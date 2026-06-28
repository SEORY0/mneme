---
type: format-family
title: "openthread meshcop tlv or packet format"
description: "Descriptive format contract facts for openthread meshcop tlv or packet."
tags: ["openthread-meshcop-tlv-or-packet", "round-18"]
okf_support: 1
train_only: true
---
# Openthread Meshcop TLV Or Packet Format

## Round 18 Factual Contract

### Schema / Invariants
- MeshCoP TLVs use type-length-value records. A Channel Mask TLV contains one or more channel-mask entries, each with a channel page and a mask payload, and consumers iterate entries until the TLV value length is exhausted.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
