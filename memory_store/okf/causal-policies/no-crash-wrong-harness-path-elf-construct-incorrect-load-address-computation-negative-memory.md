---
type: causal-policy
title: "No Crash Wrong Harness Path Elf Construct Incorrect Load Address Computation Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal wrong_harness_path."
failure_class: "no_crash"
verifier_signal: "wrong_harness_path"
candidate_family: "construct"
input_format: "elf"
harness_convention: "qemu-fuzzer"
vuln_class: "incorrect-load-address-computation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrong-harness-path", "elf", "negative-memory", "round-14"]
match_keys: ["no_crash", "wrong_harness_path", "elf", "qemu-fuzzer", "incorrect-load-address-computation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Wrong Harness Path Elf Construct Incorrect Load Address Computation Negative Memory

- key: `no_crash x wrong_harness_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf]]
- related harness facts: [[qemu-fuzzer]]

## Failure Shape
A minimal ELF load-segment construction and several generic QEMU device-fuzzer byte layouts did not reach linux-user ELF loading locally. The generated verifier for this task ran an e1000e generic fuzz target, so the linux-user loaddr path appeared unreachable through the local harness.

## Policy
Treat `no_crash x wrong_harness_path` on `elf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
