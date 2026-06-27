---
type: causal-policy
title: "Wrong Sink Git Smart Protocol Both Images Crash Off Target Negative Memory"
description: "Negative memory for wrong_sink with both_images_crash_off_target on git-smart-protocol inputs."
failure_class: wrong_sink
verifier_signal: both_images_crash_off_target
candidate_family: construct
input_format: git-smart-protocol
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 0
confidence: medium
tags: [wrong-sink, both-images-crash-off-target, git-smart-protocol, heap-buffer-overflow-read, negative_memory]
match_keys: [wrong-sink, both-images-crash-off-target, git-smart-protocol, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Wrong Sink Git Smart Protocol Both Images Crash Off Target Negative Memory

- key: `wrong_sink x both_images_crash_off_target`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[git-smart-protocol]]

## Dead End
Valid smart-protocol advertisements and post-advertisement responses reached libgit2's transport stack, but oversized pkt-line variants crashed an adjacent packet parser in both images rather than the target gitno buffer interface. Later receive/consume variants without the oversized advertisement stayed clean.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
