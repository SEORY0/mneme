---
type: negative-memory
title: "Aac Loas Latm Construct Then Seed Mutate No Crash Parser Reached Clean After Sbr Header Update Failure In Diagnostic Replay Invalid Sbr State Processing Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal parser_reached_clean_after_sbr_header_update_failure_in_diagnostic_replay."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_after_sbr_header_update_failure_in_diagnostic_replay"
candidate_family: "construct_then_seed_mutate"
input_format: "aac-loas-latm"
harness_convention: "libfuzzer"
vuln_class: "invalid-sbr-state-processing"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-reached-clean-after-sbr-header-update-failure-in-diagnostic-replay", "aac-loas-latm", "libfuzzer", "construct-then-seed-mutate", "invalid-sbr-state-processing", "negative-memory", "round-33"]
match_keys: ["no_crash", "parser_reached_clean_after_sbr_header_update_failure_in_diagnostic_replay", "aac-loas-latm", "libfuzzer", "construct-then-seed-mutate", "invalid-sbr-state-processing", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Aac Loas Latm Construct Then Seed Mutate No Crash Parser Reached Clean After Sbr Header Update Failure In Diagnostic Replay Invalid Sbr State Processing Negative Memory

- key: `no_crash x parser_reached_clean_after_sbr_header_update_failure_in_diagnostic_replay`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[aac-loas-latm]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid LOAS/LATM carriers were constructed for both hierarchical HE-AAC SBR and AAC-ELD with explicit SBR. Mutating SBR header start, stop, crossover, extra-header, limiter, and low-delay grid fields reached SBR header resets and unsuccessful header-update statuses in diagnostic replay, but the official vulnerable build still exited cleanly. The missing trigger is likely a deeper relation between the failed update and subsequent SBR frame data or envelope scalar processing, rather than the outer LOAS/LATM transport envelope.

## Policy
Treat `no_crash x parser_reached_clean_after_sbr_header_update_failure_in_diagnostic_replay` on `aac-loas-latm` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `parser_reached_clean_after_sbr_header_update_failure_in_diagnostic_replay`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_after_sbr_header_update_failure_in_diagnostic_replay`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[aac-loas-latm]]. LOAS frames contain a sync and mux-length envelope around LATM AudioMuxElement data. A StreamMuxConfig can precede each raw payload and carries AudioSpecificConfig fields such as object type, sampling-frequency index, channel configuration, and SBR signaling. PayloadLengthInfo is followed by raw AAC/SBR bits without a byte-alignment boundary. SBR headers carry start and stop frequency bands, crossover band, optional frequency-scale and noise-band fields, and optional limiter fields; AAC-ELD uses a low-delay SBR header path while HE-AAC uses hierarchical SBR signaling.

## Harness Contract
Use [[libfuzzer]]. The active target opens the FDK-AAC decoder in LOAS/LATM mode, feeds the entire input byte stream through the decoder fill API, and repeatedly calls the decode-frame API until the stream is consumed or rejected. The harness does not use FuzzedDataProvider, a leading selector byte, multiple files, or a wrapper archive.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 25 attempts.
- Scope: generator repair and basin avoidance only.
