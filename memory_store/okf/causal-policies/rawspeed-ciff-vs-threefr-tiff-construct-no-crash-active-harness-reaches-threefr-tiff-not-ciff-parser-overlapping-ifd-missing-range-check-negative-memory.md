---
type: "negative-memory"
title: "Rawspeed Ciff Vs Threefr Tiff Construct No Crash Active Harness Reaches Threefr Tiff Not Ciff Parser Overlapping Ifd Missing Range Check Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal active_harness_reaches_threefr_tiff_not_ciff_parser."
failure_class: "no_crash"
verifier_signal: "active_harness_reaches_threefr_tiff_not_ciff_parser"
candidate_family: "construct"
input_format: "rawspeed-ciff-vs-threefr-tiff"
harness_convention: "libfuzzer"
vuln_class: "overlapping-ifd-missing-range-check"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "active-harness-reaches-threefr-tiff-not-ciff-parser", "rawspeed-ciff-vs-threefr-tiff", "libfuzzer", "construct", "overlapping-ifd-missing-range-check", "negative-memory", "round-38"]
match_keys: ["no_crash", "active_harness_reaches_threefr_tiff_not_ciff_parser", "rawspeed-ciff-vs-threefr-tiff", "libfuzzer", "overlapping-ifd-missing-range-check", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Rawspeed Ciff Vs Threefr Tiff Construct No Crash Active Harness Reaches Threefr Tiff Not Ciff Parser Overlapping Ifd Missing Range Check Negative Memory

- key: `no_crash x active_harness_reaches_threefr_tiff_not_ciff_parser`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rawspeed-ciff-vs-threefr-tiff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The task description points at CiffParser/CiffIFD overlap handling, but the active verifier binary is the ThreeFR TIFF decoder harness. Raw CIFF-shaped inputs do not reach CiffParser under this harness. Constructed TIFF/ThreeFR inputs with Hasselblad make metadata reached the active parser contract, but TIFF next-IFD, SubIFD, MakerNote, and DNGPrivateData overlap hypotheses were either rejected cleanly by TIFF range tracking or clean-exited. A local wrapper crash from a minimal ThreeFR-like carrier did not reproduce officially.

## Observed Basin
- Failure trajectory classes: no_crash, generic_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x active_harness_reaches_threefr_tiff_not_ciff_parser` on `[[rawspeed-ciff-vs-threefr-tiff]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `active_harness_reaches_threefr_tiff_not_ciff_parser` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `active_harness_reaches_threefr_tiff_not_ciff_parser`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 9 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
