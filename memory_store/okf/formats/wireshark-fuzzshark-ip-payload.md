---
type: format
title: "Wireshark Fuzzshark Ip Payload"
access_scope: generate
confidence: medium
tags: ["wireshark-fuzzshark-ip-payload", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Wireshark Fuzzshark Ip Payload

## Round 13 Facts
- This harness accepts raw IP-family packet bytes for fuzzshark rather than a full pcap or pcapng envelope. Capture-file formats present in the source tree can run cleanly but are not the natural input contract for this image.
