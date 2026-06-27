---
type: causal-policy
title: "No Crash Heif File Processed Or Rejected Cleanly Heif Isobmff Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal heif_file_processed_or_rejected_cleanly."
failure_class: "no_crash"
verifier_signal: "heif_file_processed_or_rejected_cleanly"
candidate_family: "seed_mutate"
input_format: "heif-isobmff"
harness_convention: "afl-libfuzzer"
vuln_class: "missing-input-buffer-check"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "heif-file-processed-or-rejected-cleanly", "heif-isobmff", "negative-memory", "round-13"]
match_keys: ["no_crash", "heif_file_processed_or_rejected_cleanly", "heif-isobmff", "afl-libfuzzer", "missing-input-buffer-check", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Heif File Processed Or Rejected Cleanly Heif Isobmff Negative Memory

- key: `no_crash x heif_file_processed_or_rejected_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[heif-isobmff]]
- related harness facts: [[afl-libfuzzer]]

## Failure Shape
Valid HEIF seeds, brand mutations, short brand-only boxes, and truncated metadata boxes all reached or were rejected by the HEIF handler without a sanitizer signal. The missing trigger is likely a libheif memory-read edge after the Qt handler's canRead gate, not just a short or empty input.

## Policy
Treat `no_crash x heif_file_processed_or_rejected_cleanly` on `heif-isobmff` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `heif_file_processed_or_rejected_cleanly`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The handler recognizes ISO BMFF HEIF files by a leading file-type box with supported HEIF brands. Structurally valid seeds include ftyp plus a HEIF box graph that libheif can load and decode; short ftyp-only carriers reach the handler but are rejected by libheif as unsupported or incomplete.

## Harness Contract
The kimgio HEIF AFL-compatible wrapper feeds the whole PoC as QBuffer data to the Qt image handler. The handler peeks at the header through canRead, then reads all remaining bytes and passes the memory buffer to libheif. There is no front selector.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x heif_file_processed_or_rejected_cleanly`
- related format facts: [[heif-isobmff]]
- related harness facts: [[afl-libfuzzer]]

### Failure Shape Delta
Valid HEIF seeds, brand mutations, short brand-only boxes, and truncated metadata boxes all reached or were rejected by the HEIF handler without a sanitizer signal. The missing trigger is likely a libheif memory-read edge after the Qt handler's canRead gate, not just a short or empty input.

### Format Contract Delta
The handler recognizes ISO BMFF HEIF files by a leading file-type box with supported HEIF brands. Structurally valid seeds include ftyp plus a HEIF box graph that libheif can load and decode; short ftyp-only carriers reach the handler but are rejected by libheif as unsupported or incomplete.

### Harness Contract Delta
The kimgio HEIF AFL-compatible wrapper feeds the whole PoC as QBuffer data to the Qt image handler. The handler peeks at the header through canRead, then reads all remaining bytes and passes the memory buffer to libheif. There is no front selector.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
