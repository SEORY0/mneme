---
type: causal-policy
title: "Mruby Script Construct Official Target Match After Both Crash Variants Signed Length Bigint Load Verified Recovery"
description: "Round 13 verified recovery for generic_crash with verifier signal official_target_match_after_both_crash_variants."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_both_crash_variants"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "libfuzzer raw mruby source"
vuln_class: "signed-length-bigint-load"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match-after-both-crash-variants", "mruby-script", "construct", "verified-recovery", "round-13"]
match_keys: ["generic_crash", "official_target_match_after_both_crash_variants", "mruby-script", "libfuzzer raw mruby source", "signed-length-bigint-load", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# Mruby Script Construct Official Target Match After Both Crash Variants Signed Length Bigint Load Verified Recovery

## Policy
For `generic_crash x official_target_match_after_both_crash_variants`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a syntactically valid mruby source file containing a single enormous integer literal that is compiled into a bigint pool entry. The successful family uses a base form that makes the serialized bigint length cross the signed-byte boundary in the VM load path while avoiding the broader both-build crash seen with smaller decimal variants. The vulnerable VM interprets the length as negative; the fixed VM treats it as unsigned and exits cleanly.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The input is plain mruby source text, not bytecode or protobuf. Large integer literals are compiled into bigint pool entries and loaded by the VM at runtime. Literal base and digit count affect the serialized bigint representation and whether the crash is the target or an off-target both-build failure.

## Harness Contract
- The fuzzer passes the whole file as mruby source to the mruby_fuzzer target. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving. Syntax must compile far enough for the VM to execute the literal load path.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
## Round 13 Reinforcement

- key: `generic_crash x official_target_match_after_both_crash_variants`
- candidate family: `construct`
- related format facts: [[mruby-script]]
- related harness facts: [[libfuzzer-raw-mruby-source]]

### Procedure Delta
Use a syntactically valid mruby source file containing a single enormous integer literal that is compiled into a bigint pool entry. The successful family uses a base form that makes the serialized bigint length cross the signed-byte boundary in the VM load path while avoiding the broader both-build crash seen with smaller decimal variants. The vulnerable VM interprets the length as negative; the fixed VM treats it as unsigned and exits cleanly.

### Format Contract Delta
The input is plain mruby source text, not bytecode or protobuf. Large integer literals are compiled into bigint pool entries and loaded by the VM at runtime. Literal base and digit count affect the serialized bigint representation and whether the crash is the target or an off-target both-build failure.

### Harness Contract Delta
The fuzzer passes the whole file as mruby source to the mruby_fuzzer target. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving. Syntax must compile far enough for the VM to execute the literal load path.

### Evidence Shape
- Support: additional round-13 official target match.
- Scope: generator repair for the same failure-keyed basin.
