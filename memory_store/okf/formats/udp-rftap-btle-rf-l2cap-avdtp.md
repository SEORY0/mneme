---
type: format-family
title: "UDP Rftap Btle Rf L2cap Avdtp"
description: "Round 36 factual format contract for udp-rftap-btle-rf-l2cap-avdtp."
tags: ["udp-rftap-btle-rf-l2cap-avdtp", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# UDP Rftap Btle Rf L2cap Avdtp

## Round 36 Factual Contract

### Schema / Invariants
- For this harness, a successful BTLE input can be wrapped as a UDP datagram whose payload is RFtap. RFtap begins with a fixed magic, a header-length word count, flags declaring which optional parameters are present, and an input-chosen pcap data-link type. The Bluetooth LE RF link type carries RF metadata followed by a normal LE link-layer frame; the LE frame includes an access address before the data PDU header. L2CAP connectionless data contains a protocol/service selector before the higher-layer payload, and AVDTP is selected by its standard Bluetooth service identifier.

### Harness Links
- [[libfuzzer-fuzzshark-ip-proto-udp]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
