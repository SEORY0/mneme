---
type: harness
title: "Libfuzzer Ndpi Process Packet"
access_scope: generate
confidence: medium
tags: ["libfuzzer-ndpi-process-packet", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Ndpi Process Packet

## Round 13 Facts
- The fuzz_process_packet harness initializes one nDPI flow, calls ndpi_detection_process_packet once on the raw input bytes, then serializes detected flow data. It expects the input to start at the IP header; TCP payload begins after the header length encoded in the TCP data-offset field.

## Round 28 Input Contract

- The fuzz_process_packet libFuzzer target initializes one nDPI flow and passes the entire raw input buffer to ndpi_detection_process_packet. There is no FuzzedDataProvider layout, selector byte, or file container; TCP payload begins after the IP and TCP header lengths encoded in the packet itself.

## Round 28 Format Links
- [[ipv4-tcp-http-response]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
