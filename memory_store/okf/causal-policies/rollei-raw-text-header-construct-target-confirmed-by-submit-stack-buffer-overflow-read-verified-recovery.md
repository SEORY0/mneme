---
type: causal-policy
title: "Rollei Raw Text Header Construct Target Confirmed By Submit Stack Buffer Overflow Read Verified Recovery"
description: "Round 13 verified recovery for wrong_sink with verifier signal target_confirmed_by_submit."
failure_class: "wrong_sink"
verifier_signal: "target_confirmed_by_submit"
candidate_family: "construct"
input_format: "rollei-raw-text-header"
harness_convention: "libfuzzer whole-buffer LibRaw"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-confirmed-by-submit", "rollei-raw-text-header", "construct", "verified-recovery", "round-13"]
match_keys: ["wrong_sink", "target_confirmed_by_submit", "rollei-raw-text-header", "libfuzzer whole-buffer LibRaw", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# Rollei Raw Text Header Construct Target Confirmed By Submit Stack Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x target_confirmed_by_submit`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the raw camera signature that selects the Rollei metadata parser, then provide a header line that exactly fills the parser line buffer without a delimiter or line terminator. The vulnerable buffer datastream returns that line without ensuring string termination, so the later metadata parser string scan reads past the local line buffer. The fixed build adds the missing termination and exits cleanly.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The Rollei path is selected by a textual raw-camera signature near the start of the file. The parser then reads newline-delimited ASCII-style metadata records with optional key/value delimiters and an end-of-header marker. Recognized keys set geometry and thumbnail offsets, but this bug can be reached during metadata parsing before a complete image payload is needed.

## Harness Contract
- The fuzzer passes the entire PoC buffer to LibRaw open_buffer, then would call unpack and dcraw_process only if opening succeeds. There is no leading selector, checksum, path argument, or FuzzedDataProvider carving; the file signature selects the parser path.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
## Round 13 Reinforcement

- key: `wrong_sink x target_confirmed_by_submit`
- candidate family: `construct`
- related format facts: [[rollei-raw-text-header]]
- related harness facts: [[libfuzzer-whole-buffer-libraw]]

### Procedure Delta
Use the raw camera signature that selects the Rollei metadata parser, then provide a header line that exactly fills the parser line buffer without a delimiter or line terminator. The vulnerable buffer datastream returns that line without ensuring string termination, so the later metadata parser string scan reads past the local line buffer. The fixed build adds the missing termination and exits cleanly.

### Format Contract Delta
The Rollei path is selected by a textual raw-camera signature near the start of the file. The parser then reads newline-delimited ASCII-style metadata records with optional key/value delimiters and an end-of-header marker. Recognized keys set geometry and thumbnail offsets, but this bug can be reached during metadata parsing before a complete image payload is needed.

### Harness Contract Delta
The fuzzer passes the entire PoC buffer to LibRaw open_buffer, then would call unpack and dcraw_process only if opening succeeds. There is no leading selector, checksum, path argument, or FuzzedDataProvider carving; the file signature selects the parser path.

### Evidence Shape
- Support: additional round-13 official target match.
- Scope: generator repair for the same failure-keyed basin.
