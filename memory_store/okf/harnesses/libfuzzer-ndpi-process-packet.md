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
