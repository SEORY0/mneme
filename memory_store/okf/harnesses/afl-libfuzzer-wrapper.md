---
type: harness-contract
title: "Afl Libfuzzer Wrapper harness"
description: "Input contract facts for Afl Libfuzzer Wrapper."
tags: ["afl-libfuzzer-wrapper", "round-6"]
okf_support: 3
---
# Afl Libfuzzer Wrapper Harness

## Round 6 Input Contract
- The AFL-style reader fuzzer writes the raw input to a temporary pcap file, opens it with libpcap, allocates an exact-size buffer for each captured packet, and feeds packets through the normal nDPI workflow with tunnel decoding enabled.
- The AFL-style wrapper invokes FujiDecompressorFuzzer on the copied raw input. The fuzzer constructs RawImage metadata from the front of the file, installs a CFA table, creates image data, runs Fuji decompression, and treats RawSpeed exceptions as non-crashing outcomes.
- The wrapper invokes fuzz_pkcs15_encode on the copied raw input. Short arbitrary bytes do not select the tagged encoding path.

## Format Links
- [[pcap-openvpn]]
- [[pkcs15-encode-fuzzer-input]]
- [[rawspeed-decompressor-envelope]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
