---
type: format
title: "Xaac Encoder Fdp"
input_format: xaac-encoder-fdp
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Xaac Encoder Fdp

## Schema
- The logical input is not an AAC file. Front-loaded FuzzedDataProvider fields choose encoder parameters such as sample rate, channel mode, bit-rate, audio object type, SBR/USAC/DRC flags, and then supply synthetic PCM frame bytes or fill values.
