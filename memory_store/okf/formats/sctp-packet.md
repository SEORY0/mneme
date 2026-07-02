---
type: format-family
title: "Sctp Packet"
description: "Round 7 factual format contract for sctp-packet."
resource: cybergym://format/sctp-packet
tags: ["sctp-packet", "format-contract", "round-7", "round-16"]
okf_support: 3
train_only: true
---
# Sctp Packet

## Round 7 Factual Contract

### Schema / Invariants
- The SCTP harness expects packets with a common header followed by SCTP chunks. Chunk headers carry a
type, flags, and length; many parser paths require a valid association verification tag and stage-
specific handshake state before later chunks are interpreted deeply.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- SCTP packets have a common header followed by typed chunks with chunk-local lengths and padding. In this client harness the common header is synthesized by the target for the fuzzed packet, so the file bytes after the selector represent chunk payloads rather than a full wire packet.

### Harness Links
- [[afl-libfuzzer-compatible]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- SCTP packets have a common header followed by typed chunks. INIT chunks carry an initiate tag, receive window, stream counts, initial sequence value, and optional parameters such as cookie-preserve. ERROR chunks carry nested causes such as stale-cookie with a staleness value.

### Harness Links
- [[afl-file]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- SCTP packets use a common header followed by one or more typed chunks. Each chunk has a type, flags, a chunk-local length, body fields determined by the chunk type, and alignment padding. Later-stage chunks such as DATA/I-DATA, SACK, FORWARD-TSN, RE-CONFIG, ASCONF, HEARTBEAT, SHUTDOWN, ERROR, and ABORT are interpreted meaningfully only after the association state and verification tag are plausible.

### Harness Links
- [[afl-libfuzzer-compatible]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- SCTP packets consist of a common header followed by padded typed chunks. In the connect fuzzer, the fuzzed bytes after the selector are chunk records rather than a full SCTP packet because the harness synthesizes the common header and verification tag. Later chunk families such as DATA/I-DATA, SACK, FORWARD-TSN, STREAM-RESET, ASCONF, ASCONF-ACK, and packet-dropped reports require compatible association state and negotiated feature support before their nested fields are interpreted deeply.

### Harness Links
- [[afl-libfuzzer-compatible]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- SCTP listen inputs are a common header followed by typed chunks. COOKIE-ECHO is formed by reusing a state-cookie parameter body as a chunk: a chunk header, a packed state cookie, embedded original INIT and INIT-ACK material, and a digest trailer. Common and chunk headers use network-order wire fields. The packed state cookie stores timeval and lifetime fields in host representation, while its saved ports and verification tag must match the raw common-header representation. A non-stale cookie also needs a coherent address type and AF_CONN address fields so the listener can reconstruct the peer endpoint.

### Harness Links
- [[afl-style-usrsctp-listen-fuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
