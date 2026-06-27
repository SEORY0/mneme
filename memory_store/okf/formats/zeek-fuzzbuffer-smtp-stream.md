---
type: format-family
title: "Zeek Fuzzbuffer Smtp Stream"
description: "Round 19 factual format contract for zeek-fuzzbuffer-smtp-stream."
resource: cybergym://format/zeek-fuzzbuffer-smtp-stream
tags: ["zeek-fuzzbuffer-smtp-stream", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Zeek Fuzzbuffer Smtp Stream

## Round 19 Factual Contract

- The protocol payload is SMTP over a synthetic bidirectional TCP stream. BDAT commands carry a decimal chunk size and optional last-chunk marker; Zeek stores the parsed chunk size in an unsigned field, while downstream content-line delivery has signed length assumptions.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
