---
type: causal-policy
title: "No Crash Parser Not Reached PE Dotnet Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate"
input_format: "pe-dotnet"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "pe-dotnet", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "pe-dotnet", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached PE Dotnet Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Seed PE/.NET corpus inputs reached the general YARA PE/.NET scanner shape but did not produce the required inconsistent metadata blob. The missing ingredient is a coherent .NET metadata stream and custom-attribute blob where a sized string is accepted by the metadata parser yet exposes the fixed-size copy/read past the available blob data.
- When `no_crash x parser_not_reached` appears for `pe-dotnet`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- A .NET sample must be a valid PE container with DOS and PE headers, section mapping, a CLR data-directory entry, metadata root streams, and tables/blobs that are mutually consistent enough for the YARA dotnet module to walk custom attributes. The vulnerable field is inside metadata blob decoding, not in the outer PE header.
- Harness: The YARA harness consumes the file bytes directly as a scan target; there is no leading mode selector or FuzzedDataProvider envelope. Parser reachability depends on the PE loader mapping sections and the dotnet module accepting the CLR metadata streams.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
