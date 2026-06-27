---
type: causal-policy
title: "No Crash Protobuf Text To Mruby Source Proto Target Reached No Target Crash Negative Memory"
description: "Negative memory for no_crash with proto_target_reached_no_target_crash on protobuf-text-to-mruby-source inputs."
failure_class: no_crash
verifier_signal: proto_target_reached_no_target_crash
candidate_family: construct
input_format: protobuf-text-to-mruby-source
harness_convention: libfuzzer-libprotobuf-mutator
vuln_class: stack-use-after-realloc
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, proto-target-reached-no-target-crash, protobuf-text-to-mruby-source, stack-use-after-realloc, negative_memory]
match_keys: [no-crash, proto-target-reached-no-target-crash, protobuf-text-to-mruby-source, stack-use-after-realloc]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Protobuf Text To Mruby Source Proto Target Reached No Target Crash Negative Memory

- key: `no_crash x proto_target_reached_no_target_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[protobuf-text-to-mruby-source]]

## Dead End
Raw Ruby source snippets were rejected by the selected protobuf target before conversion. Text-format Function messages that generated high local pressure, nested begin blocks, branch-heavy code, expression temporaries, and repeated builtin method calls either compiled and executed cleanly or hit ordinary compiler limits. The missing gate is likely a generated Ruby shape that causes a Proc or VM call frame to extend the stack while a register pointer remains live; the available converter grammar did not expose that shape in the tested families.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
