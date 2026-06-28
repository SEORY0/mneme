---
type: negative-memory
title: "No Crash Clean Exit Pkcs15 Reader Corpus Opensc Pkcs15 Reader Stream Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal clean_exit_pkcs15_reader_corpus."
failure_class: "no_crash"
verifier_signal: "clean_exit_pkcs15_reader_corpus"
candidate_family: "seed_replay"
input_format: "opensc-pkcs15-reader-stream"
harness_convention: "honggfuzz/libfuzzer-driver"
vuln_class: "buffer-underread"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-pkcs15-reader-corpus", "opensc-pkcs15-reader-stream", "honggfuzz-libfuzzer-driver", "seed-replay", "negative-memory", "round-19"]
match_keys: ["no-crash", "clean-exit-pkcs15-reader-corpus", "opensc-pkcs15-reader-stream", "honggfuzz-libfuzzer-driver", "buffer-underread"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Clean Exit Pkcs15 Reader Corpus Opensc Pkcs15 Reader Stream Negative Memory

- key: `no_crash x clean_exit_pkcs15_reader_corpus`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-stream]]
- harnesses: [[honggfuzz-libfuzzer-driver]]

## Failure Shape
Several in-repo PKCS#15 reader corpus seeds exercised the harness without crashing. The missing condition is a TCOS-specific card binding and response sequence that reaches the decipher/read-behind path, not just generic PKCS#15 reader traffic.

## Policy
Treat `no_crash x clean_exit_pkcs15_reader_corpus` on `opensc-pkcs15-reader-stream` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
