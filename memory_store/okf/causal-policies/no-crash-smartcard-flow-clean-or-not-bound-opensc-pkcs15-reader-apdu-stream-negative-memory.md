---
type: negative-memory
title: "No Crash Smartcard Flow Clean Or Not Bound Opensc Pkcs15 Reader Apdu Stream Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal smartcard_flow_clean_or_not_bound."
failure_class: "no_crash"
verifier_signal: "smartcard_flow_clean_or_not_bound"
candidate_family: "seed_replay_pkcs15_reader_corpus"
input_format: "opensc-pkcs15-reader-apdu-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "smartcard-flow-clean-or-not-bound", "opensc-pkcs15-reader-apdu-stream", "libfuzzer", "seed-replay-pkcs15-reader-corpus", "negative-memory", "round-19"]
match_keys: ["no-crash", "smartcard-flow-clean-or-not-bound", "opensc-pkcs15-reader-apdu-stream", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Smartcard Flow Clean Or Not Bound Opensc Pkcs15 Reader Apdu Stream Negative Memory

- key: `no_crash x smartcard_flow_clean_or_not_bound`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-apdu-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Existing PKCS#15 reader corpus streams were accepted or rejected cleanly and did not drive TCOS PIN insertion into the malformed EF_PWDD record loop. The missing relation is a TCOS-v3 card binding path that reaches a PIN object, selects the password-description file, and returns a short or malformed record whose declared internal TLV lengths exceed the returned APDU data.

## Policy
Treat `no_crash x smartcard_flow_clean_or_not_bound` on `opensc-pkcs15-reader-apdu-stream` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
