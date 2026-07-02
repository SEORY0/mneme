---
type: causal-policy
title: "Sctp Packet Seed Replay And Construct No Crash Packet Injected Clean Exit Length Validation Order Negative Memory"
description: "Round 34 negative memory for sctp-packet when no_crash pairs with packet_injected_clean_exit."
failure_class: "no_crash"
verifier_signal: "packet_injected_clean_exit"
candidate_family: "seed_replay_and_construct"
input_format: "sctp-packet"
harness_convention: "afl-libfuzzer-compatible"
vuln_class: "length-validation-order"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "packet-injected-clean-exit", "sctp-packet", "afl-libfuzzer-compatible", "seed-replay-and-construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "packet-injected-clean-exit", "sctp-packet", "afl-libfuzzer-compatible", "seed-replay-and-construct", "length-validation-order", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Sctp Packet Seed Replay And Construct No Crash Packet Injected Clean Exit Length Validation Order Negative Memory

- key: `no_crash x packet_injected_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sctp-packet]]
- related harness facts: [[afl-libfuzzer-compatible]]

## Round 34 Negative Support

- key: `no_crash x packet_injected_clean_exit`
- outcome: persistent failure / basin to avoid
- candidate family: `seed_replay_and_construct`
- vulnerability class: `length-validation-order`
- related format facts: [[sctp-packet]]
- related harness facts: [[afl-libfuzzer-compatible]]

### Failure Shape
The active connect fuzzer accepted or ignored all tested stateful SCTP inputs without surfacing the length-before-validation crash. Distinct attempts included direct and selector-corrected corpus replay, DATA and I-DATA chunk length underflows, control chunk length sweeps across handshake stages, packet-dropped reports with short embedded-packet bodies, INIT-ACK outer and nested length corruptions, and source-guided checks of supported ASCONF/reconfiguration length walkers. The strongest source-level underflow candidate was gated by a negotiated feature not enabled by the harness-injected handshake.

### Policy
Treat `no_crash x packet_injected_clean_exit` on `sctp-packet` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
SCTP packets consist of a common header followed by padded typed chunks. In the connect fuzzer, the fuzzed bytes after the selector are chunk records rather than a full SCTP packet because the harness synthesizes the common header and verification tag. Later chunk families such as DATA/I-DATA, SACK, FORWARD-TSN, STREAM-RESET, ASCONF, ASCONF-ACK, and packet-dropped reports require compatible association state and negotiated feature support before their nested fields are interpreted deeply.

### Harness Contract
The active binary is the multi-stage SCTP connect fuzzer. The first input byte selects a handshake stage; the harness creates an SCTP client, injects canned peer handshake packets according to that stage, prepends its own SCTP common header to the remaining input, and injects the result into usrsctp. Inputs below the minimum size or above the maximum are skipped before packet injection.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `seed_replay_and_construct`.
- Verifier key: `no_crash x packet_injected_clean_exit`.
- Vulnerability class: `length-validation-order`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
