---
type: causal-policy
title: "Nef Tiff Construct Parser Reached Nikon Decompressor Target Match Assertion Or Bounds Failure In Decompressor Verified Recovery"
description: "Round 23 verified recovery for generic_crash with verifier signal parser_reached_nikon_decompressor_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_nikon_decompressor_target_match"
candidate_family: "construct"
input_format: "nef-tiff"
harness_convention: "libfuzzer"
vuln_class: "assertion-or-bounds-failure-in-decompressor"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-nikon-decompressor-target-match", "nef-tiff", "libfuzzer", "construct", "verified-recovery", "round-23"]
match_keys: ["generic-crash", "parser-reached-nikon-decompressor-target-match", "nef-tiff", "libfuzzer", "assertion-or-bounds-failure-in-decompressor"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Nef Tiff Construct Parser Reached Nikon Decompressor Target Match Assertion Or Bounds Failure In Decompressor Verified Recovery

- key: `generic_crash x parser_reached_nikon_decompressor_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[nef-tiff]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a compact TIFF/NEF-like envelope that selects the Nikon compressed raw path while declaring an odd image width. Keep enough image metadata and strip payload for the decoder to instantiate the Nikon decompressor; the vulnerable path proceeds into decompression with an invalid width relationship that the fixed build rejects or avoids.

## Policy
For `generic_crash x parser_reached_nikon_decompressor_target_match` on `nef-tiff`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `nef-tiff` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `nef-tiff` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 1 attempts.
- Scope: generator repair only.
