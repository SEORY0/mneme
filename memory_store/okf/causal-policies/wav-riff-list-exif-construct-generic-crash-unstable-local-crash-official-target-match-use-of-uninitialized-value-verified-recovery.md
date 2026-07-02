---
type: causal-policy
title: "Wav Riff List Exif Construct Generic Crash Unstable Local Crash Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal unstable_local_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "unstable_local_crash_official_target_match"
candidate_family: "construct"
input_format: "wav-riff-list-exif"
harness_convention: "libfuzzer-sndfile-virtual-io"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "unstable-local-crash-official-target-match", "wav-riff-list-exif", "libfuzzer-sndfile-virtual-io", "construct", "use-of-uninitialized-value", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "unstable_local_crash_official_target_match", "wav-riff-list-exif", "libfuzzer-sndfile-virtual-io", "use-of-uninitialized-value", "generic-crash", "unstable-local-crash-official-target-match", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Wav Riff List Exif Construct Generic Crash Unstable Local Crash Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x unstable_local_crash_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[wav-riff-list-exif]]
- related harness facts: [[libfuzzer-sndfile-virtual-io]]

## Failure Shape
Build a valid RIFF/WAVE container with a coherent PCM format chunk so libsndfile reaches the WAV header parser, then place a LIST chunk whose payload starts with the EXIF list marker. Inside that EXIF subchunk, use a string-valued EXIF record and make its declared string length much larger than the remaining record payload while still below the parser's fixed scratch-buffer rejection threshold. This reaches the EXIF string sink and makes the vulnerable parser consume/sink beyond the real EXIF string payload; the fixed build exits cleanly.

## Policy
When `generic_crash x unstable_local_crash_official_target_match` appears for `wav-riff-list-exif` under `libfuzzer-sndfile-virtual-io`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[wav-riff-list-exif]]` format contract and `[[libfuzzer-sndfile-virtual-io]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `wav-riff-list-exif` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 46 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
