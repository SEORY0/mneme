---
type: harness
title: "Libfuzzer Ndpi Process Packet"
harness_convention: libfuzzer-ndpi-process-packet
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Ndpi Process Packet

## Input Contract
- For `ipv4-tcp-http-response`, The fuzz_process_packet harness initializes one nDPI flow, calls ndpi_detection_process_packet once on the raw input bytes, then serializes detected flow data. It expects the input to start at the IP header; TCP payload begins after the header length encoded in the TCP data-offset field.
