---
type: causal-policy
title: "IVF AV1 Seed Sweep Construct No Crash Decoder Clean After Seed Sweep Generated Forward Keyframes And Thread Selector Mutations Incorrect Reference Frame State Negative Memory"
description: "Negative memory for ivf-av1 candidates that ended in no_crash with verifier signal decoder_clean_after_seed_sweep_generated_forward_keyframes_and_thread_selector_mutations."
failure_class: "no_crash"
verifier_signal: "decoder_clean_after_seed_sweep_generated_forward_keyframes_and_thread_selector_mutations"
candidate_family: "seed-sweep+construct"
input_format: "ivf-av1"
harness_convention: "libfuzzer"
vuln_class: "incorrect-reference-frame-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-clean-after-seed-sweep-generated-forward-keyframes-and-thread-selector-mutations", "ivf-av1", "libfuzzer", "seed-sweep-construct", "incorrect-reference-frame-state", "negative-memory", "round-32"]
match_keys: ["no-crash", "decoder-clean-after-seed-sweep-generated-forward-keyframes-and-thread-selector-mutations", "ivf-av1", "libfuzzer", "seed-sweep-construct", "incorrect-reference-frame-state", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# IVF AV1 Seed Sweep Construct No Crash Decoder Clean After Seed Sweep Generated Forward Keyframes And Thread Selector Mutations Incorrect Reference Frame State Negative Memory

- key: `no_crash x decoder_clean_after_seed_sweep_generated_forward_keyframes_and_thread_selector_mutations`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[ivf-av1]]
- related harness facts: [[libfuzzer]]

## Policy
Treat `no_crash x decoder_clean_after_seed_sweep_generated_forward_keyframes_and_thread_selector_mutations` for `[[ivf-av1]]` under `[[libfuzzer]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: The harness and IVF parser were exercised with minimized corpus seeds, the full bundled corpus including larger multi-frame IVF streams, locally generated streams with lagged references, alt-ref, forward-keyframe, and keyframe-filter options, plus header-byte thread-count mutations. All variants decoded or were rejected cleanly. The missing relation appears to be a valid show-existing-frame reset where frame context must be reloaded from the post-refresh next_ref_frame_map entry; the attempted streams did not drive that exact reference-map transition into a sanitizer-visible failure.
3. Rebuild around `[[ivf-av1]]` and `[[libfuzzer]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- The accepted carrier is an IVF-style AV1 stream. Parser reachability requires a coherent IVF container followed by valid encoded AV1 frame payloads. The target state is not exposed by arbitrary frame-size/header mutation; it likely requires a semantically valid multi-frame sequence involving show-existing-frame behavior, keyframe reset state, reference map refresh flags, and frame-context reuse.

## Harness Contract
- The libFuzzer target feeds raw input bytes through an in-memory file. It reads an IVF-style header before decoder initialization, derives the decoder thread count from a header-controlled value in threaded builds, then passes each IVF frame payload to the AV1 decoder and drains output frames. There is no FuzzedDataProvider layout, mode-selector byte outside the IVF header, or checksum requirement.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 295.
