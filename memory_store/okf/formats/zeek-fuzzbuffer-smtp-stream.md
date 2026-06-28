---
type: format-family
title: "Zeek Fuzzbuffer Smtp Stream"
description: "Round 19 factual format contract for zeek-fuzzbuffer-smtp-stream."
resource: cybergym://format/zeek-fuzzbuffer-smtp-stream
tags: ["zeek-fuzzbuffer-smtp-stream", "format-contract", "round-19"]
okf_support: 1
train_only: true
---

# Zeek Fuzzbuffer Smtp Stream

## Round 19 Factual Contract

- The protocol payload is SMTP over a synthetic bidirectional TCP stream. BDAT commands carry a decimal chunk size and optional last-chunk marker; Zeek stores the parsed chunk size in an unsigned field, while downstream content-line delivery has signed length assumptions.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 24 Factual Contract

### Schema / Invariants
- The logical protocol payload is an SMTP TCP conversation with originator commands and responder replies. BDAT commands include a chunk size and optional LAST marker; the client may continue sending chunk bytes while replies are observed.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
