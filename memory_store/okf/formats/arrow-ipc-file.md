---
type: format-family
title: "arrow-ipc-file format"
description: "Structure and reachability facts for arrow-ipc-file."
resource: "cybergym://format/arrow-ipc-file"
tags: ["arrow-ipc-file", "round-31"]
okf_support: 1
train_only: true
---
# Arrow Ipc File Format

## Round 31 Factual Contract

### Schema / Invariants
- Arrow IPC file inputs use the file magic/footer framing and a footer block table that points to record-batch messages. A record-batch message carries a FlatBuffer header with FieldNode entries in preorder and Buffer metadata entries for the flattened array layout. With older IPC metadata, REE parent arrays can carry parent validity-buffer metadata even though the modern REE logical layout has no parent bitmap. REE data is represented as a parent node followed by run-ends and values child nodes; the children remain ordinary Arrow arrays and are validated before the REE-specific parent null-count invariant.

### Harness Links
- [[libfuzzer-raw-arrow-ipc]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
