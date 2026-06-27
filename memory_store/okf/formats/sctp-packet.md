---
type: format-family
title: "Sctp Packet"
description: "Round 7 factual format contract for sctp-packet."
resource: cybergym://format/sctp-packet
tags: ["sctp-packet", "format-contract", "round-7", "round-16"]
okf_support: 2
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
