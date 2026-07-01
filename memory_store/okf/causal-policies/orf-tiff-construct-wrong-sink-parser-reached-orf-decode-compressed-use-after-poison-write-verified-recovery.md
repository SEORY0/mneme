---
type: causal-policy
title: "Orf Tiff Construct Wrong Sink Parser Reached Orf Decode Compressed Use After Poison Write Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_orf_decode_compressed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_orf_decode_compressed"
candidate_family: "construct"
input_format: "orf-tiff"
harness_convention: "libfuzzer"
vuln_class: "use-after-poison-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-orf-decode-compressed", "orf-tiff", "libfuzzer", "construct", "use-after-poison-write", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_orf_decode_compressed", "orf-tiff", "libfuzzer", "use-after-poison-write", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Orf Tiff Construct Wrong Sink Parser Reached Orf Decode Compressed Use After Poison Write Verified Recovery

- key: `wrong_sink x parser_reached_orf_decode_compressed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[orf-tiff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a minimal TIFF-derived Olympus raw carrier with byte order and directory framing accepted by the TIFF parser, Olympus make/model identification accepted by OrfDecoder, a single valid strip range, and compression metadata that selects the compressed ORF decoder path. Use an invalid small odd image width with enough strip bytes to feed the bit pump. The compressed decoder processes pixels in pairs without first validating that the row dimensions can support the paired write, so the odd-pixel write crosses into poisoned padding; the fixed build rejects the bad dimensions before processing.

## Policy
When `wrong_sink x parser_reached_orf_decode_compressed` appears for `orf-tiff` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[orf-tiff]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `orf-tiff` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
