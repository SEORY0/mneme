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

## Round 30 Factual Contract

### Schema / Invariants
- OpenThread NCP UART inputs are raw UART byte streams containing HDLC-flagged Spinel frames. Each Spinel frame begins with a header byte, a packed command id, a packed property id for property commands, and property-specific data. `STREAM_NET` and `STREAM_NET_INSECURE` carry a little-endian length-prefixed IPv6 packet followed by optional metadata. Thread on-mesh network entries are inserted as an IPv6 prefix, prefix length, stable flag, and route flags after local network-data changes are enabled.

### Harness Links
- [[libfuzzer-afl-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
