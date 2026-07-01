---
type: causal-policy
title: "PDF Construct Wrong Sink Official Target Match After Local Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal official_target_match_after_local_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "official_target_match_after_local_sink_mismatch"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "official-target-match-after-local-sink-mismatch", "pdf", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "official_target_match_after_local_sink_mismatch", "pdf", "libfuzzer", "heap-buffer-overflow-read", "wrong-sink", "official-target-match-after-local-sink-mismatch", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# PDF Construct Wrong Sink Official Target Match After Local Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x official_target_match_after_local_sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a valid renderable PDF with a normal catalog, page tree, text content stream, and a Type1 font resource whose descriptor references an embedded font stream. Keep the document xref valid, but place the referenced embedded font stream as a forward object after the xref/trailer area and truncate the font stream body while its declared stream length remains positive. Rendering text forces Poppler to load the embedded font through a bulk stream read; the vulnerable build accepts the exhausted memory substream relation while the fixed build rejects or clamps it.

## Policy
When `wrong_sink x official_target_match_after_local_sink_mismatch` appears for `pdf` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[pdf]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `pdf` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 14 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
