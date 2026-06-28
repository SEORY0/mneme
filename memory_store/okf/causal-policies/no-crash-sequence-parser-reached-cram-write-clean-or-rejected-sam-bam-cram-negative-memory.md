---
type: negative-memory
title: "No Crash Sequence Parser Reached Cram Write Clean Or Rejected Sam Bam Cram Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal sequence-parser-reached-cram-write-clean-or-rejected."
failure_class: "no-crash"
verifier_signal: "sequence-parser-reached-cram-write-clean-or-rejected"
candidate_family: "construct"
input_format: "sam-bam-cram"
harness_convention: "libfuzzer-raw-htslib-hts-open"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "sequence-parser-reached-cram-write-clean-or-rejected", "sam-bam-cram", "libfuzzer-raw-htslib-hts-open", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "sequence-parser-reached-cram-write-clean-or-rejected", "sam-bam-cram", "libfuzzer-raw-htslib-hts-open", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Sequence Parser Reached Cram Write Clean Or Rejected Sam Bam Cram Negative Memory

- key: `no-crash x sequence-parser-reached-cram-write-clean-or-rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sam-bam-cram]]
- harnesses: [[libfuzzer-raw-htslib-hts-open]]

## Failure Shape
SAM text variants were normalized or rejected before exposing an internal negative coordinate. Minimal binary alignment variants reached the CRAM write loop, but without an available reference the writer switched to non-reference mode or rejected the coordinate before the described reference-array understep occurred.

## Policy
Treat `no-crash x sequence-parser-reached-cram-write-clean-or-rejected` on `sam-bam-cram` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
