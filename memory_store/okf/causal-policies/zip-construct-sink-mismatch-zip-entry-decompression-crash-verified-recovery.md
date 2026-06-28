---
type: causal-policy
title: "Zip Construct Sink Mismatch Zip Entry Decompression Crash Verified Recovery"
description: "Round 14 server-verified recovery for zip keyed by generic_crash x sink_mismatch."
failure_class: "generic_crash"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "zip"
harness_convention: "libfuzzer"
vuln_class: "zip-entry-decompression-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "sink-mismatch", "zip", "libfuzzer", "construct", "zip-entry-decompression-crash", "verified-recovery", "round-14"]
match_keys: ["generic_crash", "sink_mismatch", "zip", "libfuzzer", "zip-entry-decompression-crash", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 14
---
# Zip Construct Sink Mismatch Zip Entry Decompression Crash Verified Recovery

- key: `generic_crash x sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[zip]]
- related harness facts: [[libfuzzer]]

## Policy
When `zip` under `libfuzzer` reaches `sink_mismatch` from `generic_crash`, keep the accepted carrier and retarget the single invariant named by the verified recovery. This policy is verifier-gated by vulnerable-build failure and fixed-build non-match behavior.

## Procedure
1. Preserve the harness contract `[[libfuzzer]]` and format contract `[[zip]]`; do not switch container families once parser reachability is proven.
2. Apply the verified recovery: Construct a valid archive directory with an image-like entry name so the document recognizer treats it as an archive-backed document, but make the entry compressed and shorter than the declared decompressed payload. Opening/rendering the page forces archive-entry decompression and the vulnerable short-compressed-data handling.
3. Keep mutations focused on the gate relation: declared size versus available data, selector versus subparser, structure count versus actual records, lifetime ownership, or sink-specific state.
4. If local labels report `wrong_sink` while the same parser branch is reached, submit once to check the official target match before discarding the candidate.
5. If the fixed image also fails, shrink back to the smallest boundary relation and avoid broad randomization.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not promote this as a byte recipe; it is a format-gate and sink-invariant relation.

## Evidence Shape
- Support: one server-verified Round 14 solve.
- Candidate family: construct.
