---
type: causal-policy
title: "CPython Sre Match Payload Post Init Retarget Verified Recovery"
description: "Round 9 retarget recovery for wrong_sink with verifier signal target_warning_but_official_both_nonzero."
failure_class: "wrong_sink"
verifier_signal: "target_warning_but_official_both_nonzero"
candidate_family: "construct-retarget"
input_format: "CPython sre-match fuzzer byte stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-warning-but-official-both-nonzero", "cpython-sre-match-fuzzer-byte-stream", "retarget", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "target_warning_but_official_both_nonzero", "CPython sre-match fuzzer byte stream", "libfuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# CPython Sre Match Payload Post Init Retarget Verified Recovery

## Policy
For `wrong_sink x target_warning_but_official_both_nonzero` on the CPython sre-match fuzzer, escape the selector-only initialization basin by providing a non-empty match payload. The official verifier accepted a candidate that drives the precompiled regex match callback after initialization rather than relying on the shared interpreter startup warning.

## Procedure
1. Preserve the harness contract: the first byte selects a precompiled regex pattern modulo the table, and all remaining bytes become the Python bytes object passed to the selected pattern's `match` method.
2. Avoid selector-only or tiny inputs that fail during interpreter/module initialization on both images. Include a substantive post-selector payload so the input-specific callback reaches `PyObject_GetAttrString(pattern, "match")` and `PyObject_CallOneArg`.
3. Prefer boundary-oriented payloads for the fixed regex table, such as long word-like spans and separator text, to keep execution in the regex matching path rather than the compile path.
4. Treat local both-image or initialization-looking warnings as non-authoritative for this basin; the official submit verdict is the deciding signal.

## Format Contract
- The byte stream is not Python source and not a regex pattern. It is selector plus subject bytes for one fixed regex from the harness table.
- The selected pattern table includes anchors, word-boundary, groups, character classes, and simple repetitions. The payload must be long enough to exercise matching rather than only startup.

## Harness Contract
- `LLVMFuzzerInitialize` starts CPython before the input-specific callback. The callback precompiles the fixed regex table on first use, selects a pattern from the first byte, constructs a bytes object from the remaining input, and calls the selected pattern's `match` method.

## Negative Memory
- Do not promote selector-only crashes; they are likely shared initialization failures or both-image warnings.
- Do not switch to the sre-compile harness shape. This task's active surface is fixed-pattern matching.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 retarget check with official target match after the worker trace failed.
- Scope: generator repair for the same failure-keyed basin.
