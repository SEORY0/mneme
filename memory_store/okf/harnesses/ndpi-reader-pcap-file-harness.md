---
type: harness-contract
title: "Ndpi Reader Pcap File Harness harness"
description: "Input contract facts for ndpi-reader-pcap-file-harness."
tags: ["ndpi-reader-pcap-file-harness", "round-20"]
okf_support: 1
---
# Ndpi Reader Pcap File Harness Harness

## Round 20 Input Contract
- The harness writes raw input to a temporary pcap file, opens it with pcap_open_offline, rejects unsupported datalinks, allocates exact-size buffers for each captured packet, processes all packets through ndpi_workflow_process_packet, then tears down flow trees.

## Round 20 Format Links
- [[pcap-containing-ip-packets]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
