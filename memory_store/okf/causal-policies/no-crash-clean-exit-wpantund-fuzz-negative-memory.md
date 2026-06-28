---
type: negative-memory
title: "No Crash Clean Exit Wpantund Fuzz Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "seed_mutate"
input_format: "wpantund-fuzz"
harness_convention: "afl-libfuzzer-file"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "wpantund-fuzz", "afl-libfuzzer-file", "seed-mutate", "negative-memory", "round-22"]
match_keys: ["no-crash", "clean-exit", "wpantund-fuzz", "afl-libfuzzer-file", "use-after-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Clean Exit Wpantund Fuzz Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wpantund-fuzz]]
- harnesses: [[afl-libfuzzer-file]]

## Failure Shape
The bundled config and NCP corpus seeds all satisfied the top-level selector contract but exited cleanly. The config mode exercised setting parsing and MainLoop construction; the NCP mode exercised HDLC-framed socket input and special wait/fast-forward commands. None of the tried seeds produced the add-then-remove on-mesh-prefix state needed to call the removal handler on a stale multimap entry.

## Policy
Treat `no_crash x clean_exit` on `wpantund-fuzz` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, wrapper-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 22.
- Scope: generator repair and basin avoidance only.
