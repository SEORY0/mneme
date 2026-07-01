---
type: format-family
title: "Openthread Ncp Uart format"
description: "Round 8 descriptive format facts for openthread-ncp-uart."
resource: cybergym://format/openthread-ncp-uart
tags: ["openthread-ncp-uart", "round-8"]
okf_support: 3
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

## Round 32 Factual Contract

### Schema / Invariants
- NCP UART input is an HDLC-lite byte stream with flag-delimited frames, escaped control bytes, and a frame check sequence. The decoded payload is a Spinel frame with a header byte, packed command id, packed property id for property commands, and property-specific data. STREAM_NET carries a little-endian length-prefixed IPv6 datagram followed by optional metadata. THREAD_ON_MESH_NETS insertion carries an IPv6 prefix, prefix length, stable flag, and route flags. Mesh-local on-mesh checks use the device mesh-local prefix derived from the extended PAN ID, while local network-data changes may require later registration processing before leader network data reflects them.

### Harness Links
- [[afl-libfuzzer-ncp-uart-received]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 33 Factual Contract

### Schema / Invariants
- OpenThread NCP UART input is an HDLC-lite stream of flag-delimited Spinel frames. Decoded Spinel property frames contain a header byte, a packed command id, a packed property id, and property-specific values. THREAD_ON_MESH_NETS and THREAD_OFF_MESH_ROUTES insertions carry an IPv6 prefix, prefix length, stable flag, and route flags after local network-data changes are enabled. SERVER_SERVICES insertion carries an enterprise number, length-prefixed service data, stable flag, and length-prefixed server data. Thread Network Data TLVs use a one-byte type/stable discriminator and a one-byte length, with nested Prefix, HasRoute, Service, and Server TLVs governed by their advertised lengths.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
