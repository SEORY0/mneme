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

## Round 25 Factual Contract

### Schema / Invariants
- LXC config input is line-oriented key/value text. Time namespace offset keys parse a signed integer prefix and a residual unit suffix; accepted unit names include short time units that are later trimmed and compared as strings.

### Harness Links
- [[libfuzzer-tempfile]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Schema / Invariants
- LXC config is line-oriented key/value text. Rootfs options are parsed as a comma-separated mount-option string; LXC-specific options such as idmapped mount paths are recognized inside that value before generic mount-option parsing continues.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
