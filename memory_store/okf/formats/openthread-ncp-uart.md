---
type: format-family
title: "Openthread Ncp Uart format"
description: "Round 8 descriptive format facts for openthread-ncp-uart."
resource: cybergym://format/openthread-ncp-uart
tags: ["openthread-ncp-uart", "round-8"]
okf_support: 1
---
# Openthread Ncp Uart Format

## Round 8 Factual Contract

### Schema / Invariants
- OpenThread NCP UART fuzzing expects a stream of NCP/Spinel UART bytes, not CLI text. The vulnerable logic compares encoded Thread network-data TLVs; each TLV has a type/stability discriminator, a length, and nested value/sub-TLV regions whose advertised lengths govern iteration.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

