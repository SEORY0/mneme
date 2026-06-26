---
type: format-family
title: "Lxc Config Text"
description: "Round 7 factual format contract for lxc-config-text."
resource: cybergym://format/lxc-config-text
tags: ["lxc-config-text", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Lxc Config Text

## Round 7 Factual Contract

### Schema / Invariants
- LXC configuration is line-oriented key/value text. Signal-related keys route their value through a
signal-name parser that recognizes ordinary signal names and realtime signal forms.

### Harness Links
- [[afl-libfuzzer-tempfile]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
