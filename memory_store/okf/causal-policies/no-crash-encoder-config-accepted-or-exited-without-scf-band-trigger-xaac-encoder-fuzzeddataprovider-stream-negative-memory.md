---
type: negative-memory
title: "No Crash Encoder Config Accepted Or Exited Without Scf Band Trigger Xaac Encoder Fuzzeddataprovider Stream Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal encoder_config_accepted_or_exited_without_scf_band_trigger."
failure_class: "no_crash"
verifier_signal: "encoder_config_accepted_or_exited_without_scf_band_trigger"
candidate_family: "construct"
input_format: "xaac-encoder-fuzzeddataprovider-stream"
harness_convention: "libfuzzer"
vuln_class: "numeric-domain-error-in-encoder-analysis"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "encoder-config-accepted-or-exited-without-scf-band-trigger", "xaac-encoder-fuzzeddataprovider-stream", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "encoder-config-accepted-or-exited-without-scf-band-trigger", "xaac-encoder-fuzzeddataprovider-stream", "libfuzzer", "numeric-domain-error-in-encoder-analysis"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Encoder Config Accepted Or Exited Without Scf Band Trigger Xaac Encoder Fuzzeddataprovider Stream Negative Memory

- key: `no_crash x encoder_config_accepted_or_exited_without_scf_band_trigger`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[xaac-encoder-fuzzeddataprovider-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Constructed FuzzedDataProvider tails covered several encoder configurations, including USAC/SBR-leaning, AAC-LC-like, high-bitrate, DRC-enabled, and shorter-payload variants. None reached the scale-factor-band form-factor zero/gain-bound condition. The decoder seed corpus is a red herring for this verifier-selected encoder target.

## Policy
Treat `no_crash x encoder_config_accepted_or_exited_without_scf_band_trigger` on `xaac-encoder-fuzzeddataprovider-stream` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
