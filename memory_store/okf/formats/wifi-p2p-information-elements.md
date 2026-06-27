---
type: format-family
title: wifi-p2p-information-elements format
description: Structure and reachability facts for wifi-p2p-information-elements inputs.
tags: [wifi-p2p-information-elements]
okf_support: 0
---
# Wifi P2P Information Elements Format

## Round 10 Factual Contract

### Schema / Invariants
- P2P attributes live inside a Wi-Fi vendor-specific IE with the P2P OUI/type. Group Info contains length-prefixed client descriptors; each descriptor carries device and interface addresses, capability/configuration fields, primary device type, a count-prefixed secondary device-type list, and a WPS Device Name TLV.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
