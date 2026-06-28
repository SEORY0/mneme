---
type: format
title: "Haproxy Config"
access_scope: generate
confidence: medium
tags: ["haproxy-config", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Haproxy Config

## Round 13 Facts
- HAProxy config parsing tokenizes one logical line into an output buffer plus an args array. Quoting, backslash escaping, comments, and environment expansion are handled before keyword dispatch; too many logical words are reported after output-buffer sizing has succeeded.

## Round 22 Factual Contract

### Schema / Invariants
- The input is raw HAProxy configuration text. The parser reads file lines into a growable buffer, uses C-string length to determine the logical line end, and later trims a presumed trailing newline by writing near that computed end. Embedded string terminators can make physical line length and logical parser length disagree.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
