---
type: negative-memory
title: "No Crash Parser Reached Seed Then Image Rejected After Tail Libraw Fuzzed Provider Plus Raw Image Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal parser_reached_seed_then_image_rejected_after_tail."
failure_class: "no_crash"
verifier_signal: "parser_reached_seed_then_image_rejected_after_tail"
candidate_family: "seed_mutate"
input_format: "libraw-fuzzed-provider-plus-raw-image"
harness_convention: "libfuzzer"
vuln_class: "buffer-overrun"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-seed-then-image-rejected-after-tail", "libraw-fuzzed-provider-plus-raw-image", "libfuzzer", "seed-mutate", "negative-memory", "round-22"]
match_keys: ["no-crash", "parser-reached-seed-then-image-rejected-after-tail", "libraw-fuzzed-provider-plus-raw-image", "libfuzzer", "buffer-overrun"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Parser Reached Seed Then Image Rejected After Tail Libraw Fuzzed Provider Plus Raw Image Negative Memory

- key: `no_crash x parser_reached_seed_then_image_rejected_after_tail`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libraw-fuzzed-provider-plus-raw-image]]
- harnesses: [[libfuzzer]]

## Failure Shape
Real RAF seeds plus abnormal chromatic-aberration option tails did not reach the target; the reader reported image end-of-file after option-tail insertion. The attempt used the correct remaining-bytes model but likely changed a seed whose format stores or validates trailing file data, so the next attempt should use a raw seed format tolerant of trailing bytes or patch option bytes without disturbing image-size assumptions.

## Policy
Treat `no_crash x parser_reached_seed_then_image_rejected_after_tail` on `libraw-fuzzed-provider-plus-raw-image` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

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
