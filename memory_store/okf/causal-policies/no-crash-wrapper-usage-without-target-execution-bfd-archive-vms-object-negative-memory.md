---
type: causal-policy
title: "No Crash Wrapper Usage Without Target Execution Bfd Archive Vms Object Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal wrapper_usage_without_target_execution."
failure_class: "no_crash"
verifier_signal: "wrapper_usage_without_target_execution"
candidate_family: "construct"
input_format: "bfd-archive-vms-object"
harness_convention: "honggfuzz-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-usage-without-target-execution", "bfd-archive-vms-object", "negative-memory", "round-13"]
match_keys: ["no_crash", "wrapper_usage_without_target_execution", "bfd-archive-vms-object", "honggfuzz-file", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Wrapper Usage Without Target Execution Bfd Archive Vms Object Negative Memory

- key: `no_crash x wrapper_usage_without_target_execution`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[bfd-archive-vms-object]]
- related harness facts: [[honggfuzz-file]]

## Failure Shape
A GNU archive-shaped probe with VMS-like counted-string data did not reach a target crash. The local arvo wrapper emitted honggfuzz usage text instead of clearly running the BFD fuzzer on the file, and the hand-built archive did not establish a valid VMS object/archive member state.

## Policy
Treat `no_crash x wrapper_usage_without_target_execution` on `bfd-archive-vms-object` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_usage_without_target_execution`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The vulnerable BFD helper reads a counted string as a leading length byte followed by that many payload bytes; the bug is triggered when the available record length excludes the count byte but the count equals the remaining byte count. Reaching it requires a valid VMS object or VMS library record path, not just arbitrary counted-string bytes.

## Harness Contract
The source fuzzer writes raw input to a temporary file, opens it with BFD auto-detection, and calls archive-format checking. The arvo image wrapper for this task appears to be honggfuzz-oriented and did not produce the normal one-input libFuzzer execution transcript.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x wrapper_usage_without_target_execution`
- related format facts: [[bfd-archive-vms-object]]
- related harness facts: [[honggfuzz-file]]

### Failure Shape Delta
A GNU archive-shaped probe with VMS-like counted-string data did not reach a target crash. The local arvo wrapper emitted honggfuzz usage text instead of clearly running the BFD fuzzer on the file, and the hand-built archive did not establish a valid VMS object/archive member state.

### Format Contract Delta
The vulnerable BFD helper reads a counted string as a leading length byte followed by that many payload bytes; the bug is triggered when the available record length excludes the count byte but the count equals the remaining byte count. Reaching it requires a valid VMS object or VMS library record path, not just arbitrary counted-string bytes.

### Harness Contract Delta
The source fuzzer writes raw input to a temporary file, opens it with BFD auto-detection, and calls archive-format checking. The arvo image wrapper for this task appears to be honggfuzz-oriented and did not produce the normal one-input libFuzzer execution transcript.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
