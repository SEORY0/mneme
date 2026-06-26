---
type: causal-policy
title: "No Crash Interpreter Error Before Sink Postscript Pfb Font Stream Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal interpreter_error_before_sink."
failure_class: "no_crash"
verifier_signal: "interpreter_error_before_sink"
candidate_family: "construct"
input_format: "PostScript/PFB font stream"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "interpreter-error-before-sink", "postscript-pfb-font-stream", "negative-memory", "round-6"]
match_keys: ["no_crash", "interpreter_error_before_sink", "PostScript/PFB font stream", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Interpreter Error Before Sink Postscript Pfb Font Stream Negative Memory

- key: `no_crash x interpreter_error_before_sink`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-pfb-font-stream]]

## Failure Shape
- The candidates reached Ghostscript startup but failed as malformed jobs or did not drive the PFBDecode limit path. Hand-built PFB and PostScript filter envelopes were insufficient to create a valid font stream that both passed interpreter gates and violated the stream limit invariant.

## Policy
Treat `no_crash x interpreter_error_before_sink` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
