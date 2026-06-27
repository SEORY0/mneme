---
type: causal-policy
title: "Gif Construct Target Stack Reached Global Buffer Overflow Read Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal target_stack_reached."
failure_class: "wrong_sink"
verifier_signal: "target_stack_reached"
candidate_family: "construct"
input_format: "gif"
harness_convention: "honggfuzz-file"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-stack-reached", "gif", "construct", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "target_stack_reached", "gif", "honggfuzz-file", "global-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Gif Construct Target Stack Reached Global Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x target_stack_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Preserve a syntactically valid GIF envelope with a tiny logical screen, matching palette, and an
  interlaced image descriptor.
1. Encode image data that remains valid LZW but emits more pixels than the tiny interlaced frame can
  consume, so decoded-row advancement walks beyond the fixed interlace pass tables while the fixed
  build rejects the pass overflow.

## Format Contract
- GIF parsing requires a valid signature, logical screen descriptor, palette relationship, image
  descriptor, LZW minimum code size, sub-block image data, and terminator.
- The vulnerable path is entered by selecting interlaced image decoding and producing decoded
  pixels, not by corrupting the trailer.

## Harness Contract
- The selected wrapper runs the GIF loader on the file bytes directly.
- The input is a complete GIF byte stream; there is no fuzzer selector byte or outer container
  beyond the image format itself.

## Related Knowledge
- Format facts: [[gif]]
- Harness facts: [[honggfuzz-file]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
