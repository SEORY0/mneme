---
type: harness-contract
title: "Afl Wrapper harness"
description: "Input contract facts for afl-wrapper."
tags: ["afl-wrapper"]
okf_support: 2
---
# Afl Wrapper Harness

## Round 10 Input Contract
- The verifier output indicated a required directory path instead of a normal libFuzzer single input file. No FuzzedDataProvider layout was observed; the blocker was the wrapper invocation contract.
- Source extraction required skipping an absolute symlink before runner metadata could be recovered. The active verifier binary read raw input through fuzzshark configured for the UDP dissector in the ip.proto table, not a direct IEEE1905 dissector or Ethernet ethertype wrapper.

## Round 10 Format Links
- [[file-magic-corpus-directory]]
- [[wireshark-fuzzshark-udp-payload]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (ovs-ofctl-flow-text)

- The harness rejects inputs that are too short, not NUL-terminated, contain newlines after the selector, or contain embedded NUL bytes in the flow string. It maps the first byte to a flow-mod command and passes the remaining C string to parse_ofp_flow_mod_str before encoding the flow mod.

## Round 21 Format Links (ovs-ofctl-flow-text)
- [[ovs-ofctl-flow-text]]

## Round 21 Notes (ovs-ofctl-flow-text)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (jpeg-exif)

- The GraphicsMagick fuzzer is compiled around a coder/enhance target that reads bytes into a Magick image blob and may write or transform the decoded image. The local generated wrapper may expect AFL-style replay semantics rather than a plain file for some coder targets.

## Round 21 Format Links (jpeg-exif)
- [[jpeg-exif]]

## Round 21 Notes (jpeg-exif)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
