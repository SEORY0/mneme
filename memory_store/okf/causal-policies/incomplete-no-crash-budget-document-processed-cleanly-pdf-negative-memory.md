---
type: negative-memory
title: "Incomplete No Crash Budget Document Processed Cleanly Pdf Negative Memory"
description: "Round 21 negative memory for incomplete-no-crash-budget with verifier signal document-processed-cleanly."
failure_class: "incomplete-no-crash-budget"
verifier_signal: "document-processed-cleanly"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-after-free-or-invalid-reference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["incomplete-no-crash-budget", "document-processed-cleanly", "pdf", "libfuzzer", "construct", "negative-memory", "round-21"]
match_keys: ["incomplete-no-crash-budget", "document-processed-cleanly", "pdf", "libfuzzer", "use-after-free-or-invalid-reference"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# Incomplete No Crash Budget Document Processed Cleanly Pdf Negative Memory

- key: `incomplete-no-crash-budget x document-processed-cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- harnesses: [[libfuzzer]]

## Failure Shape
A minimal PDF with a text drawing operator and intentionally problematic font resource processed cleanly. The missing trigger is likely a text drawing error that occurs after the string operand reference is captured but before show completion, causing the operand stack to clear while the string is still used.

## Policy
Treat `incomplete-no-crash-budget x document-processed-cleanly` on `pdf` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
