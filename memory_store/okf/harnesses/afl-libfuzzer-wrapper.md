---
type: harness-contract
title: "Afl Libfuzzer Wrapper harness"
description: "Input contract facts for Afl Libfuzzer Wrapper."
tags: ["afl-libfuzzer-wrapper", "round-6"]
okf_support: 4
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

## Round 10 Input Contract
- The verifier runs a RawSpeed AFL-style parser/get-decoder/decode wrapper on raw file bytes. An empty file aborts in harness setup, while nonempty candidate containers are parsed or rejected without a target sanitizer report.

## Round 10 Format Links
- [[rawspeed-camera-file-or-jpeg-container]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 12 Input Contract
- The AFL-style wrapper feeds the raw file bytes to FujiDecompressorFuzzer. The fuzzer constructs a RawImage, installs the CFA table, creates image storage, runs Fuji decompression, and treats RawSpeed exceptions as non-crashing outcomes.

## Round 12 Format Links
- [[rawspeed-fuji-decompressor-envelope]]

## Round 12 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (samsung-srw-tiff-raw)

- The RawSpeed harness passes raw bytes to RawParser, asks for a decoder from camera metadata, then runs raw decode and metadata decode. There is no mode byte; the file envelope must select the SRW decoder naturally.

## Round 21 Format Links (samsung-srw-tiff-raw)
- [[samsung-srw-tiff-raw]]

## Round 21 Notes (samsung-srw-tiff-raw)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 22 Input Contract
- The image wrapper runs fuzzshark_ip on a single raw input file. The configured dissector target is IP, so the input is treated as an IP-layer packet rather than as a pcap file or an Ethernet frame. WCP is not directly registered as an IP payload protocol in the inspected source.

## Format Links
- [[ip-carried-wcp]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 28 Input Contract

- The active target is an AFL-wrapped libFuzzer xmlReader-for-file binary. It reads the PoC as raw fuzzer bytes, parses them with libxml2's ByteStream helper, writes the carved file-content string to a temporary file, calls xmlReaderForFile with the carved encoding and options, then repeatedly calls xmlTextReaderRead and simple node accessors. There is no FuzzedDataProvider tail layout.

## Round 28 Format Links
- [[libxml2-xml-reader-byte-stream]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
