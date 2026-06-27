---
type: format
title: "Wireshark Fuzzshark Ip Payload"
input_format: wireshark-fuzzshark-ip-payload
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Wireshark Fuzzshark Ip Payload

## Schema
- This harness accepts raw IP-family packet bytes for fuzzshark rather than a full pcap or pcapng envelope. Capture-file formats present in the source tree can run cleanly but are not the natural input contract for this image.
