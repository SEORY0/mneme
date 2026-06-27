---
type: format-family
title: "ieee802154-thread-mle-frame format"
description: "Structure and reachability facts for ieee802154-thread-mle-frame."
resource: cybergym://format/ieee802154-thread-mle-frame
tags: ["ieee802154-thread-mle-frame"]
okf_support: 1
---
# Ieee802154 Thread MLE Frame Format

## Round 9 Factual Contract

### Schema / Invariants
- The relevant payload is an IEEE 802.15.4 frame carrying Thread/MLE data.
- MLE TLVs have type and length fields; the Route TLV includes a router-id sequence, router-id mask,
  and per-router route data, and the vulnerable invariant concerns route data count exceeding the
  implementation buffer capacity.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
