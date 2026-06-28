---
type: format
title: "Rollei Raw Text Header"
access_scope: generate
confidence: medium
tags: ["rollei-raw-text-header", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Rollei Raw Text Header

## Round 13 Facts
- The Rollei path is selected by a textual raw-camera signature near the start of the file. The parser then reads newline-delimited ASCII-style metadata records with optional key/value delimiters and an end-of-header marker. Recognized keys set geometry and thumbnail offsets, but this bug can be reached during metadata parsing before a complete image payload is needed.

## Round 22 Factual Contract

### Schema / Invariants
- The Rollei raw path is a text-header style format: an identifying signature is followed by newline-delimited metadata lines. Parser reachability depends on the signature and on preserving the line-oriented envelope; the crash relation is an unterminated metadata line at the local buffer boundary.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
