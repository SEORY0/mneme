---
type: harness-contract
title: "Afl Style Usrsctp Listen Fuzzer"
description: "Round 36 factual harness contract for afl-style-usrsctp-listen-fuzzer."
tags: ["afl-style-usrsctp-listen-fuzzer", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Afl Style Usrsctp Listen Fuzzer

## Round 36 Input Contract
- The AFL-style target reads the file as one raw SCTP packet and passes it unchanged to usrsctp_conninput after initializing an AF_CONN passive listener. There is no FuzzedDataProvider carving and no mode selector. Fuzzing builds bypass cookie HMAC validation, but endpoint lookup, COOKIE-ECHO tag and port checks, state-cookie address state, and embedded handshake material still need to be coherent. The harness intentionally exits nonzero when the listener association is established, and the local verifier can label that path as no_crash, so the vuln/fix exit split from submit is the authoritative oracle.

## Round 36 Format Links
- [[sctp-packet]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
