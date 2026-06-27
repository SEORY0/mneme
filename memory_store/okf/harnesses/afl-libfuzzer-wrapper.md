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

## Round 9 Input Contract
- The AFL-style fuzzer writes the raw bytes to a temporary file, opens it with BFD using auto target
  detection, checks archive format, and closes it.
- It does not carve the input or consume fields from the back.
- The AFL-style target treats the input as one raw radio PSDU, rejects frames above the radio
  maximum, initializes an OpenThread leader instance, then passes the frame to radio receive
  completion.
- There is no mode selector or back-consumed size field.
- The selected wrapper wrote raw bytes to a temporary file and invoked UPX test mode on it.
- There was no input carving.
- The output indicated the test_packed_file_fuzzer path, which reports NotPackedException or file-
  size rejection for invalid envelopes.

## Round 9 Format Links
- [[ieee802154-thread-mle-frame]]
- [[upx-packed-pe]]
- [[xcoff-archive]]

## Round 9 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
