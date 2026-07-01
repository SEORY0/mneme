---
type: format-family
title: "Openthread Cli Uart Dataset Tlv Format"
description: "Structure, build skeleton, and bug-prone areas of the openthread-cli-uart-dataset-tlv input format."
resource: "cybergym://format/openthread-cli-uart-dataset-tlv"
tags: ["openthread-cli-uart-dataset-tlv", "round-37"]
okf_support: 1
train_only: true
---
# Openthread Cli Uart Dataset Tlv Format
## Round 37 Factual Contract

### Schema / Invariants
- The CLI command is line-terminated text.
- The dataset command parses a hex string into MeshCoP TLVs; odd-length hex is accepted by treating the leading nibble as a byte.
- MeshCoP TLVs use a base type/length header, with an extended-length marker followed by an extended length field.
- Unknown TLVs are skipped, while ChannelMask normally contains channel-page, mask-length, and mask bytes.

### Harness Links
- [[honggfuzz-file-cli-uart]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
