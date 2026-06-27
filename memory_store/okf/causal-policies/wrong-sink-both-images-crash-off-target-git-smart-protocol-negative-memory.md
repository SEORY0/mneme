---
type: causal-policy
title: "Wrong Sink Both Images Crash Off Target Git Smart Protocol Negative Memory"
description: "Round 13 negative memory for wrong_sink with verifier signal both_images_crash_off_target."
failure_class: "wrong_sink"
verifier_signal: "both_images_crash_off_target"
candidate_family: "construct"
input_format: "git-smart-protocol"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "both-images-crash-off-target", "git-smart-protocol", "negative-memory", "round-13"]
match_keys: ["wrong_sink", "both_images_crash_off_target", "git-smart-protocol", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# Wrong Sink Both Images Crash Off Target Git Smart Protocol Negative Memory

- key: `wrong_sink x both_images_crash_off_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[git-smart-protocol]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid smart-protocol advertisements and post-advertisement responses reached libgit2's transport stack, but oversized pkt-line variants crashed an adjacent packet parser in both images rather than the target gitno buffer interface. Later receive/consume variants without the oversized advertisement stayed clean.

## Policy
Treat `wrong_sink x both_images_crash_off_target` on `git-smart-protocol` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crash_off_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is a Git smart transport byte stream made of pkt-lines, flush packets, ref advertisements, negotiation responses, and optional pack or sideband data. Pkt-lines use a length-prefixed ASCII envelope, and valid advertisements are needed before fetch negotiation and pack download paths run.

## Harness Contract
The fuzzer installs a fake smart subtransport whose read callback copies the raw input bytes into libgit2's network buffer. There is no outer file format or fuzzer-side carving; all structure is the Git wire protocol itself.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `wrong_sink x both_images_crash_off_target`
- related format facts: [[git-smart-protocol]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
Valid smart-protocol advertisements and post-advertisement responses reached libgit2's transport stack, but oversized pkt-line variants crashed an adjacent packet parser in both images rather than the target gitno buffer interface. Later receive/consume variants without the oversized advertisement stayed clean.

### Format Contract Delta
The input is a Git smart transport byte stream made of pkt-lines, flush packets, ref advertisements, negotiation responses, and optional pack or sideband data. Pkt-lines use a length-prefixed ASCII envelope, and valid advertisements are needed before fetch negotiation and pack download paths run.

### Harness Contract Delta
The fuzzer installs a fake smart subtransport whose read callback copies the raw input bytes into libgit2's network buffer. There is no outer file format or fuzzer-side carving; all structure is the Git wire protocol itself.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
