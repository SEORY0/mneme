---
type: format-family
title: "Wolfmqtt Datasource Stream Format"
description: "Round 26 descriptive structure and invariant facts for wolfmqtt datasource stream."
tags: ["wolfmqtt-datasource-stream", "round-26"]
okf_support: 1
train_only: true
---
# Wolfmqtt Datasource Stream Format

## Round 26 Factual Contract

### Schema / Invariants
- The target format is the fuzzing-headers datasource layout: every consumed value is preceded by a little-endian size field. Fixed-size integers and booleans consume their exact byte width after the size prefix; strings consume a size prefix followed by that many bytes and become NUL-terminated C strings through std::string. The MQTT CONNECT encoder builds a fixed header, protocol header, client-id field, optional LWT fields, optional username, and optional password into a fixed transmit buffer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
