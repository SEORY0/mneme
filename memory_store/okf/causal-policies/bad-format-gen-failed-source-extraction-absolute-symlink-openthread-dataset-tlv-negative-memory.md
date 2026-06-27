---
type: causal-policy
title: "Bad Format Gen Failed Source Extraction Absolute Symlink Openthread Dataset Tlv Negative Memory"
description: "Round 15 negative memory for bad_format with verifier signal gen_failed_source_extraction_absolute_symlink."
failure_class: "bad_format"
verifier_signal: "gen_failed_source_extraction_absolute_symlink"
candidate_family: "infrastructure_blocked"
input_format: "openthread-dataset-tlv"
harness_convention: "unavailable-after-gen-extraction-failure"
vuln_class: "tlv-length-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["bad-format", "gen-failed-source-extraction-absolute-symlink", "openthread-dataset-tlv", "negative-memory", "round-15"]
match_keys: ["bad_format", "gen_failed_source_extraction_absolute_symlink", "openthread-dataset-tlv", "unavailable-after-gen-extraction-failure", "tlv-length-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# Bad Format Gen Failed Source Extraction Absolute Symlink Openthread Dataset Tlv Negative Memory

- key: `bad_format x gen_failed_source_extraction_absolute_symlink`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-dataset-tlv]]
- related harness facts: [[unavailable-after-gen-extraction-failure]]

## Failure Shape
- Task generation failed while extracting the vulnerable source archive because the archive contained
  an absolute symlink. The task description indicates that the target is OpenThread Dataset TLV
  validation for Active/Pending Timestamp and Delay Timer minimum lengths, but the run directory did
  not receive the verifier metadata needed for runner verify/submit in this worker pass.

## Policy
Treat `bad_format x gen_failed_source_extraction_absolute_symlink` on `openthread-dataset-tlv` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- OpenThread operational datasets are TLV streams. Each record has a type, length, and value;
  timestamp-style TLVs and delay timer TLVs require minimum value lengths before their contents are
  interpreted. A malformed dataset can use a recognized TLV type with an undersized value to test
  those minimum-length checks.

## Harness Contract
- The intended harness could not be confirmed from a completed gen_info/verify_config pair because
  generation stopped during archive extraction. Partial source extraction showed an OpenThread tree,
  but this worker did not reconstruct the missing runner metadata or run a verifier for this task.

## Negative Memory
- Do not resubmit variants that only reproduce `gen_failed_source_extraction_absolute_symlink`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
