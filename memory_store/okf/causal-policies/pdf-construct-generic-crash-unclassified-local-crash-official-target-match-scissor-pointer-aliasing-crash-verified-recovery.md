---
type: causal-policy
title: "Pdf Construct Generic Crash Unclassified Local Crash Official Target Match Scissor Pointer Aliasing Crash Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal unclassified_local_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "unclassified_local_crash_official_target_match"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "scissor-pointer-aliasing-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "unclassified-local-crash-official-target-match", "pdf", "libfuzzer", "construct", "scissor-pointer-aliasing-crash", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "unclassified_local_crash_official_target_match", "pdf", "libfuzzer", "scissor-pointer-aliasing-crash", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Pdf Construct Generic Crash Unclassified Local Crash Official Target Match Scissor Pointer Aliasing Crash Verified Recovery

- key: `generic_crash x unclassified_local_crash_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a minimal renderable PDF with internally consistent document structure, page tree, page box, content stream length, cross-reference table, and trailer. In the page content, apply clipping paths before painting so MuPDF enters the draw-device clip path and updates the same scissor rectangle through an alias-sensitive parameter relation; the vulnerable build crashes during rendering while the fixed build exits cleanly.

## Policy
When `generic_crash x unclassified_local_crash_official_target_match` appears for `pdf` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[pdf]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `pdf` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 139, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
