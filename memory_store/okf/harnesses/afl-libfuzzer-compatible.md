---
type: harness-contract
title: "Afl Libfuzzer Compatible harness"
description: "Input contract facts for afl-libfuzzer-compatible."
tags: ["afl-libfuzzer-compatible"]
okf_support: 0
---
# Afl Libfuzzer Compatible Harness

## Round 10 Input Contract
- The first input byte selects a handshake stage when the build does not force one. The harness internally opens an SCTP client, injects canned peer handshake packets, prepends a common header with the captured verification tag to the remaining fuzz bytes, and then feeds that packet to usrsctp.

## Round 10 Format Links
- [[sctp-packet]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
