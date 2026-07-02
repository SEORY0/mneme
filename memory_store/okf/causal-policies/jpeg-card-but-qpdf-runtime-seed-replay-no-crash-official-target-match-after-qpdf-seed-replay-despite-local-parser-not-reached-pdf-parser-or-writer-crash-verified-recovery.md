---
type: causal-policy
title: "Jpeg Card But Qpdf Runtime Seed Replay No Crash Official Target Match After Qpdf Seed Replay Despite Local Parser Not Reached Pdf Parser Or Writer Crash Verified Recovery"
description: "Round 37 verified recovery for no_crash with verifier signal official_target_match_after_qpdf_seed_replay_despite_local_parser_not_reached."
failure_class: "no_crash"
verifier_signal: "official_target_match_after_qpdf_seed_replay_despite_local_parser_not_reached"
candidate_family: "seed_replay"
input_format: "jpeg-card-but-qpdf-runtime"
harness_convention: "libfuzzer"
vuln_class: "pdf-parser-or-writer-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "official-target-match-after-qpdf-seed-replay-despite-local-parser-not-reached", "jpeg-card-but-qpdf-runtime", "libfuzzer", "seed-replay", "pdf-parser-or-writer-crash", "verified-recovery", "round-37"]
match_keys: ["no_crash", "official_target_match_after_qpdf_seed_replay_despite_local_parser_not_reached", "jpeg-card-but-qpdf-runtime", "libfuzzer", "pdf-parser-or-writer-crash", "verified-recovery", "seed_replay"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Jpeg Card But Qpdf Runtime Seed Replay No Crash Official Target Match After Qpdf Seed Replay Despite Local Parser Not Reached Pdf Parser Or Writer Crash Verified Recovery

- key: `no_crash x official_target_match_after_qpdf_seed_replay_despite_local_parser_not_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[jpeg-card-but-qpdf-runtime]]
- related harness facts: [[libfuzzer]]

## Failure Shape
After runtime evidence showed the JPEG card actually executed qpdf, replay a compact in-image qpdf_extra PDF seed rather than a JPEG. The successful family is a minimal PDF-like stream and trailer carrier that preserves the qpdf raw-byte parser gate while stressing a stream length relation; the vulnerable build exits abnormally and the fixed build exits cleanly.

## Policy
When `no_crash x official_target_match_after_qpdf_seed_replay_despite_local_parser_not_reached` appears for `jpeg-card-but-qpdf-runtime` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[jpeg-card-but-qpdf-runtime]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `jpeg-card-but-qpdf-runtime` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 8 attempts.
- Candidate family: seed_replay.
- Official split: vulnerable exit 139, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
