---
type: "causal-policy"
title: "C Blosc2 Frame Construct Generic Crash Parser Reached Target Heap Overread Heap Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_target_heap_overread."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_heap_overread"
candidate_family: "construct"
input_format: "c-blosc2-frame"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-target-heap-overread", "c-blosc2-frame", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_target_heap_overread", "c-blosc2-frame", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# C Blosc2 Frame Construct Generic Crash Parser Reached Target Heap Overread Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_heap_overread`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[c-blosc2-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a valid contiguous Blosc2 frame with multiple logical chunks, internally consistent header and trailer metadata, and an offset/index chunk that the frame reader accepts. Encode the offset/index chunk as a run-length value so offset lookup succeeds under the harness, then make the selected logical chunk point to a self-consistent extended memcpy chunk header near the end of the actual frame data. The chunk header declares a payload extent that crosses the frame boundary, causing the vulnerable lazy chunk decompression path to copy past the in-memory frame while the fixed build rejects the out-of-frame extent.

## Policy
When `generic_crash x parser_reached_target_heap_overread` appears for `[[c-blosc2-frame]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[c-blosc2-frame]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[c-blosc2-frame]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 12 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
