---
type: "causal-policy"
title: "DXF Text Construct Generic Crash Parser Reached Summaryinfo Cleanup Invalid Free Uninitialized Pointer Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_summaryinfo_cleanup."
failure_class: "generic_crash"
verifier_signal: "parser_reached_summaryinfo_cleanup"
candidate_family: "construct"
input_format: "dxf-text"
harness_convention: "libfuzzer"
vuln_class: "invalid-free-uninitialized-pointer"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-summaryinfo-cleanup", "dxf-text", "libfuzzer", "construct", "invalid-free-uninitialized-pointer", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_summaryinfo_cleanup", "dxf-text", "libfuzzer", "invalid-free-uninitialized-pointer", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# DXF Text Construct Generic Crash Parser Reached Summaryinfo Cleanup Invalid Free Uninitialized Pointer Verified Recovery

- key: `generic_crash x parser_reached_summaryinfo_cleanup`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[dxf-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a text DXF document that reaches the HEADER section and sets a summary custom-property tag without the matching custom-property value. Keep the file over the DXF reader's minimum-size gate using ordinary text pairs, then end the document malformed so the DXF reader returns a critical error. The vulnerable cleanup frees the partially initialized summary property and dereferences its uninitialized value pointer; the fixed build initializes or avoids freeing that missing member.

## Policy
When `generic_crash x parser_reached_summaryinfo_cleanup` appears for `[[dxf-text]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[dxf-text]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[dxf-text]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
