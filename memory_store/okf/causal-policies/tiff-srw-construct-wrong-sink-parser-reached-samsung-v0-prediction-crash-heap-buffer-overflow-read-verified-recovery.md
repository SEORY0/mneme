---
type: "causal-policy"
title: "Tiff Srw Construct Wrong Sink Parser Reached Samsung V0 Prediction Crash Heap Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_samsung_v0_prediction_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_samsung_v0_prediction_crash"
candidate_family: "construct"
input_format: "tiff-srw"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-samsung-v0-prediction-crash", "tiff-srw", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_samsung_v0_prediction_crash", "tiff-srw", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Tiff Srw Construct Wrong Sink Parser Reached Samsung V0 Prediction Crash Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_samsung_v0_prediction_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[tiff-srw]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a minimal little-endian TIFF-style Samsung raw image that selects the SRW decoder, uses the Samsung V0 compression path, provides one strip plus a coherent per-row compressed-data table, and sets image dimensions so the final horizontal prediction block is shorter than the decompressor's fixed block width. The compressed row bits should select upward prediction so the unguarded read crosses the row boundary while the fixed build rejects or avoids the unsafe access.

## Policy
When `wrong_sink x parser_reached_samsung_v0_prediction_crash` appears for `[[tiff-srw]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[tiff-srw]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[tiff-srw]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
