---
type: format-family
title: rf4ce-over-ieee802154 format
description: "Round 23 descriptive structure and invariant facts for rf4ce-over-ieee802154."
resource: cybergym://format/rf4ce-over-ieee802154
tags: ["rf4ce-over-ieee802154", "round-23"]
okf_support: 1
train_only: true
---
# Rf4ce Over Ieee802154 Format

## Round 23 Factual Contract

### Schema / Invariants
- RF4CE NWK is carried as a heuristic payload over IEEE 802.15.4 WPAN. The NWK frame starts with a frame-control field and sequence number, optionally includes profile/vendor fields, then command or data payload. The copy-sensitive path decrypts or copies the remaining NWK payload into an internal buffer based on the reported packet length.

### Harness Links
- [[fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
