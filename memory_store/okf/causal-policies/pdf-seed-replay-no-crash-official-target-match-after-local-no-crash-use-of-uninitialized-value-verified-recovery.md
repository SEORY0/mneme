---
type: causal-policy
title: "PDF Seed Replay No Crash Official Target Match After Local No Crash Use Of Uninitialized Value Verified Recovery"
description: "Round 36 verified recovery for no_crash with verifier signal official_target_match_after_local_no_crash."
failure_class: "no_crash"
verifier_signal: "official_target_match_after_local_no_crash"
candidate_family: "seed_replay"
input_format: "pdf"
harness_convention: "libfuzzer-poppler-pdf-render"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "official-target-match-after-local-no-crash", "pdf", "libfuzzer-poppler-pdf-render", "seed-replay", "use-of-uninitialized-value", "verified-recovery", "round-36"]
match_keys: ["no_crash", "official_target_match_after_local_no_crash", "pdf", "libfuzzer-poppler-pdf-render", "use-of-uninitialized-value", "no-crash", "official-target-match-after-local-no-crash", "verified_recovery", "seed_replay", "seed-replay"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# PDF Seed Replay No Crash Official Target Match After Local No Crash Use Of Uninitialized Value Verified Recovery

- key: `no_crash x official_target_match_after_local_no_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer-poppler-pdf-render]]

## Failure Shape
Use a compact real PDF corpus carrier rather than rebuilding from scratch. Preserve the malformed but loadable xref/trailer and stream structure exactly enough for Poppler's raw-memory loader to repair/open the document and enter page rendering; avoid widening the mutation into generic parser or sanitizer crashes. The local fast verifier can report clean execution, so submit the parser-reaching seed family and rely on the vulnerable/fixed oracle.

## Policy
When `no_crash x official_target_match_after_local_no_crash` appears for `pdf` under `libfuzzer-poppler-pdf-render`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[pdf]]` format contract and `[[libfuzzer-poppler-pdf-render]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
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
- Support: 1 server-verified round 36 solve after 23 attempts.
- Candidate family: seed_replay.
- Scope: generator repair and retargeting only.
