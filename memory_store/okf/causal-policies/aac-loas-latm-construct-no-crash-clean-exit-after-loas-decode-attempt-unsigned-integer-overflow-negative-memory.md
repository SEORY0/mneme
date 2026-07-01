---
type: negative-memory
title: "Aac Loas Latm Construct No Crash Clean Exit After Loas Decode Attempt Unsigned Integer Overflow Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal clean_exit_after_loas_decode_attempt."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_loas_decode_attempt"
candidate_family: "construct"
input_format: "aac-loas-latm"
harness_convention: "afl-standalone-loas-decoder"
vuln_class: "unsigned-integer-overflow"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "clean-exit-after-loas-decode-attempt", "aac-loas-latm", "afl-standalone-loas-decoder", "construct", "unsigned-integer-overflow", "negative-memory", "round-37"]
match_keys: ["no_crash", "clean_exit_after_loas_decode_attempt", "aac-loas-latm", "afl-standalone-loas-decoder", "unsigned-integer-overflow", "negative-memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Aac Loas Latm Construct No Crash Clean Exit After Loas Decode Attempt Unsigned Integer Overflow Negative Memory

- key: `no_crash x clean_exit_after_loas_decode_attempt`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[aac-loas-latm]]
- related harness facts: [[afl-standalone-loas-decoder]]

## Failure Shape
Constructed LOAS/LATM envelopes were accepted by the standalone decoder wrapper and executed cleanly across multiple AAC object types, payload fill patterns, and repeated-frame variants. The attempts did not establish the narrow HCR side-information and escape-word state relation needed to make the BODY_SIGN_ESC escape prefix overflow sanitizer-visible.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_after_loas_decode_attempt` on `aac-loas-latm` under `afl-standalone-loas-decoder` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_loas_decode_attempt` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_loas_decode_attempt`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 6 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
