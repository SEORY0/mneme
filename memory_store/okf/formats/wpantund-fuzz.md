---
type: format-family
title: wpantund-fuzz format
description: Structure, build skeleton, and bug-prone areas of the wpantund-fuzz input format.
resource: cybergym://format/wpantund-fuzz
tags: [wpantund-fuzz, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 2
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The first byte selects a harness mode: config text, NCP socket input, or an unimplemented control-interface path. Config-mode inputs are raw wpantund configuration lines after the selector. NCP-mode inputs are byte streams containing HDLC flag-delimited frames, with a special command byte used by the fuzzer to wait for outbound frames or fast-forward simulated time.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- wpantund fuzz inputs begin with a one-byte mode selector. Config mode consumes raw configuration text after the selector. NCP mode consumes an HDLC-framed Spinel byte stream; frames are flag-delimited, escaped for flag/control bytes, and in this fuzz build carry trailing FCS bytes that are stripped without normal CRC validation. Spinel VALUE_IS, VALUE_INSERTED, and VALUE_REMOVED frames carry packed command and property identifiers followed by property-specific typed payloads.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- wpantund-fuzz inputs begin with a one-byte mode selector. NCP mode consumes an HDLC-flag-delimited Spinel UART byte stream. Spinel property callbacks use a header byte, packed command id, packed property id, and property-specific typed payload. Thread on-mesh full-list updates carry repeated length-wrapped structs containing an IPv6 prefix, prefix length, stable flag, on-mesh flags, local-origin flag, and registering locator. Empty full-list updates are represented by the property callback with no entry payload.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
