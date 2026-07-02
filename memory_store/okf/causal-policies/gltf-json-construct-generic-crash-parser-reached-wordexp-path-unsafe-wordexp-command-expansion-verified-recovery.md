---
type: "causal-policy"
title: "Gltf JSON Construct Generic Crash Parser Reached Wordexp Path Unsafe Wordexp Command Expansion Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_wordexp_path."
failure_class: "generic_crash"
verifier_signal: "parser_reached_wordexp_path"
candidate_family: "construct"
input_format: "gltf-json"
harness_convention: "libfuzzer"
vuln_class: "unsafe-wordexp-command-expansion"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-wordexp-path", "gltf-json", "libfuzzer", "construct", "unsafe-wordexp-command-expansion", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_wordexp_path", "gltf-json", "libfuzzer", "unsafe-wordexp-command-expansion", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Gltf JSON Construct Generic Crash Parser Reached Wordexp Path Unsafe Wordexp Command Expansion Verified Recovery

- key: `generic_crash x parser_reached_wordexp_path`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[gltf-json]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a minimal valid ASCII glTF JSON document with the required asset metadata and an external buffer URI. Avoid a data URI so the parser routes through external asset loading and filesystem path expansion. Use a URI form that is accepted as an external asset path and exercises shell-style word expansion in the vulnerable build; the fixed build treats the asset path safely and does not invoke the dangerous expansion behavior.

## Policy
When `generic_crash x parser_reached_wordexp_path` appears for `[[gltf-json]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[gltf-json]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[gltf-json]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 2 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
