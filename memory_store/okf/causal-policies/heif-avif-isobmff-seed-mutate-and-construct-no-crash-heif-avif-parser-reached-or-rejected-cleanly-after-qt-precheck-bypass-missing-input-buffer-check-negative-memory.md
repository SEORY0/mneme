---
type: "negative-memory"
title: "Heif Avif Isobmff Seed Mutate And Construct No Crash Heif Avif Parser Reached Or Rejected Cleanly After Qt Precheck Bypass Missing Input Buffer Check Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal heif_avif_parser_reached_or_rejected_cleanly_after_qt_precheck_bypass."
failure_class: "no_crash"
verifier_signal: "heif_avif_parser_reached_or_rejected_cleanly_after_qt_precheck_bypass"
candidate_family: "seed_mutate_and_construct"
input_format: "heif-avif-isobmff"
harness_convention: "afl-libfuzzer"
vuln_class: "missing-input-buffer-check"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "heif-avif-parser-reached-or-rejected-cleanly-after-qt-precheck-bypass", "heif-avif-isobmff", "afl-libfuzzer", "seed-mutate-and-construct", "missing-input-buffer-check", "negative-memory", "round-38"]
match_keys: ["no_crash", "heif_avif_parser_reached_or_rejected_cleanly_after_qt_precheck_bypass", "heif-avif-isobmff", "afl-libfuzzer", "missing-input-buffer-check", "negative-memory", "seed_mutate_and_construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Heif Avif Isobmff Seed Mutate And Construct No Crash Heif Avif Parser Reached Or Rejected Cleanly After Qt Precheck Bypass Missing Input Buffer Check Negative Memory

- key: `no_crash x heif_avif_parser_reached_or_rejected_cleanly_after_qt_precheck_bypass`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[heif-avif-isobmff]]
- related harness facts: [[afl-libfuzzer]]

## Failure Shape
Valid HEIF seed replay, HEIF brand rejection, truncated HEIF envelopes, HEIF metadata size and extent perturbations, auxiliary-alpha dimension mutations, AVIF brand-routing mutations, and compact AVIF duplicate-file-type constructions all exited cleanly or were rejected without a sanitizer signal. The missing trigger appears to be a deeper libheif or codec memory-safety edge reached only after the Qt handler bypasses its HEIF precheck; format recognition and simple BMFF structure violations alone were insufficient.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x heif_avif_parser_reached_or_rejected_cleanly_after_qt_precheck_bypass` on `[[heif-avif-isobmff]]` under `[[afl-libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `heif_avif_parser_reached_or_rejected_cleanly_after_qt_precheck_bypass` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `heif_avif_parser_reached_or_rejected_cleanly_after_qt_precheck_bypass`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 148 attempts.
- Candidate family: seed_mutate_and_construct.
- Scope: generator repair and basin avoidance only.
