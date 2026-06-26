---
type: causal-policy
title: No Crash Parser Reached No Crash Negative Memory
description: Negative memory for no_crash with verifier signal parser_reached_no_crash.
failure_class: no_crash
verifier_signal: parser_reached_no_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-crash, negative_memory]
match_keys: [no-crash, parser-reached-no-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Reached No Crash Negative Memory

- key: `no_crash x parser_reached_no_crash`
- outcome: persistent failure basin
- support_count: 2
- candidate_families: construct, seed-mutate
- observed_formats: opentype-cff, xslt-fuzz-entities

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Keep the accepted envelope but move from broad value changes to the feature selector or state transition described by the diagnosis. A clean exit means the parser path is real but the target state was absent.

## Diagnosed Dead Ends
- The structured fuzz-entity envelope was satisfied and stylesheets invoking format-number executed without crashing. Large numeric strings, percent/per-mille multipliers, and very long fractional patterns did not reproduce the floating-point overflow; the missing invariant is the exact numeric representation or format pattern that drives the vulnerable rounding path into sanitizer-visible overflow.
- Existing draw-fuzzer and crash corpus fonts exercised the hb-draw harness but did not reproduce the CFF negative-offset sanitizer issue. The remaining gap is constructing or mutating a CFF/CFF2 table so a negative offset leaves the leading edge outside the blob while the trailing check still passes.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.

## Round 4 Reinforcement
- key: `no_crash x parser_reached_no_crash`
- outcome: persistent failure basin
- support_count: 5
- candidate_families: construct, seed-mutate
- observed_formats: dns-wire-packet, hdf5, pdf, raw-compress-buffer, rtsp-response

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- Raw compression inputs reached the compress fuzzer but did not land on the narrow condition where compressed block bytes fit while the per-block size slot write exceeds the caller-provided destination size. Deterministic sweeps over size, compressor, and filter settings stayed in no-crash behavior before the time cap.
- Minimal PDFs with transparency group XObjects rendered successfully and did not force the pdf14 device push/pop failure path. The missing trigger is likely a resource or rendering-failure condition inside a transparency group rather than just presence of a group dictionary.
- Basic DNS packet and zone-text probes reached the Knot fuzzers but did not trigger the MemorySanitizer false-positive around memzero in wire_ctx error handling. The likely missing condition is a packet path that calls wire_ctx_read after an established wire error and then uses the zeroed destination in MSAN-visible logic.
- Raw HDF5 corpus seeds opened under the extended harness but did not expose a dataset/attribute path that reaches the vulnerable sprintf formatting. Prefixing for the alternate read harness was invalid for the active extended harness, and raw seeds remained no-crash.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
