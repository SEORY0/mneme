---
type: format
title: "Openthread Ip6 Send Or Meshcop Tlv"
access_scope: generate
confidence: medium
tags: ["openthread-ip6-send-or-meshcop-tlv", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Openthread Ip6 Send Or Meshcop Tlv

## Round 13 Facts
- MeshCoP TLVs use a type-length-value layout. Base TLVs carry a one-byte length, while extended TLVs use the extended-length marker followed by a larger length field. The described invariant is that Commissioner Dataset TLVs in MGMT_COMM_SET handling must reject extended TLV length where the destination buffer expects bounded base TLVs.
