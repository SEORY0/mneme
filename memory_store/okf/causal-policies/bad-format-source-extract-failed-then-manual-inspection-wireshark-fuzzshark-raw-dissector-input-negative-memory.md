---
type: negative-memory
title: "Bad Format Source Extract Failed Then Manual Inspection Wireshark Fuzzshark Raw Dissector Input Negative Memory"
description: "Round 22 negative memory for bad_format with verifier signal source_extract_failed_then_manual_inspection."
failure_class: "bad_format"
verifier_signal: "source_extract_failed_then_manual_inspection"
candidate_family: "none"
input_format: "wireshark-fuzzshark-raw-dissector-input"
harness_convention: "oss-fuzzshark"
vuln_class: "buffer-overread"
access_scope: generate
success_count: 0
confidence: medium
tags: ["bad-format", "source-extract-failed-then-manual-inspection", "wireshark-fuzzshark-raw-dissector-input", "oss-fuzzshark", "none", "negative-memory", "round-22"]
match_keys: ["bad-format", "source-extract-failed-then-manual-inspection", "wireshark-fuzzshark-raw-dissector-input", "oss-fuzzshark", "buffer-overread"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# Bad Format Source Extract Failed Then Manual Inspection Wireshark Fuzzshark Raw Dissector Input Negative Memory

- key: `bad_format x source_extract_failed_then_manual_inspection`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-fuzzshark-raw-dissector-input]]
- harnesses: [[oss-fuzzshark]]

## Failure Shape
The normal generation step failed during source extraction because the source archive contains an absolute symlink. Manual extraction recovered the source after excluding that symlink, but no verifier run directory was completed. Source inspection identified the BER constrained bitstring sink and the fuzzshark raw-dissector harness, but no PoC was verified.

## Policy
Treat `bad_format x source_extract_failed_then_manual_inspection` on `wireshark-fuzzshark-raw-dissector-input` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

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
