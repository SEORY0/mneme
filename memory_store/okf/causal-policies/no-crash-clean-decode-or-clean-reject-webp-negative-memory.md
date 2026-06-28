---
type: negative-memory
title: "No Crash Clean Decode Or Clean Reject Webp Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal clean-decode-or-clean-reject."
failure_class: "no-crash"
verifier_signal: "clean-decode-or-clean-reject"
candidate_family: "seed-sweep"
input_format: "webp"
harness_convention: "libfuzzer-raw-ffmpeg-webp-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-decode-or-clean-reject", "webp", "libfuzzer-raw-ffmpeg-webp-decoder", "seed-sweep", "negative-memory", "round-21"]
match_keys: ["no-crash", "clean-decode-or-clean-reject", "webp", "libfuzzer-raw-ffmpeg-webp-decoder", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Clean Decode Or Clean Reject Webp Negative Memory

- key: `no-crash x clean-decode-or-clean-reject`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[webp]]
- harnesses: [[libfuzzer-raw-ffmpeg-webp-decoder]]

## Failure Shape
Ordinary WebP still-image and animation seeds decoded or rejected cleanly under the target decoder. The missing condition is likely a malformed but decodable WebP bitstream that reaches the reference-coordinate path with ref_x or ref_y left unset rather than present as normal decoded metadata.

## Policy
Treat `no-crash x clean-decode-or-clean-reject` on `webp` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.
