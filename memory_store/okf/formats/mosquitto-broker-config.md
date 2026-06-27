---
type: format-family
title: "Mosquitto Broker Config"
description: "Round 12 factual format contract for mosquitto broker config."
resource: cybergym://format/mosquitto-broker-config
tags: ["mosquitto-broker-config", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Mosquitto Broker Config

## Round 12 Factual Contract

### Schema / Invariants
- Mosquitto broker configuration is line-oriented text with global options and listener-scoped options. Listener entries select ports and protocol, websocket support is configured with protocol directives, plugins are configured by path directives, and bridge connections require address/topic-related options.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
