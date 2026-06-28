---
type: causal-policy
title: "Generic Crash Wrapper Crash Not Reproduced Officially Capstone Disasm Selector Plus Bytes Negative Memory"
description: "Round 12 negative memory for generic_crash with verifier signal wrapper_crash_not_reproduced_officially."
failure_class: "generic_crash"
verifier_signal: "wrapper_crash_not_reproduced_officially"
candidate_family: "seed_mutate"
input_format: "capstone-disasm-selector-plus-bytes"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "wrapper-crash-not-reproduced-officially", "capstone-disasm-selector-plus-bytes", "negative-memory", "round-12"]
match_keys: ["generic_crash", "wrapper_crash_not_reproduced_officially", "capstone-disasm-selector-plus-bytes", "libfuzzer", "undefined-behavior-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# Generic Crash Wrapper Crash Not Reproduced Officially Capstone Disasm Selector Plus Bytes Negative Memory

- key: `generic_crash x wrapper_crash_not_reproduced_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[capstone-disasm-selector-plus-bytes]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A seed instruction stream with the architecture selector set to a less common backend produced a local generic crash, but official submission exited cleanly. The crash was therefore not a stable target signal for the MCInst operand issue.

## Policy
Treat `generic_crash x wrapper_crash_not_reproduced_officially` on `capstone-disasm-selector-plus-bytes` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The input is not an object file. It is a one-byte platform selector followed by raw instruction bytes for the selected Capstone architecture and mode. Corpus samples are instruction-byte snippets and need the selector prefix added for this harness.

## Harness Contract
The fuzzer caps input size, maps the first byte modulo the platform table, opens that architecture/mode, enables detail output, optionally enables alternate syntax from a selector bit, and disassembles the remaining bytes from a fixed base address.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_crash_not_reproduced_officially`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
