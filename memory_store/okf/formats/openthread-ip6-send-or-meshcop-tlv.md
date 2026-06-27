---
type: format
title: "Openthread Ip6 Send Or Meshcop Tlv"
input_format: openthread-ip6-send-or-meshcop-tlv
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Openthread Ip6 Send Or Meshcop Tlv

## Schema
- MeshCoP TLVs use a type-length-value layout. Base TLVs carry a one-byte length, while extended TLVs use the extended-length marker followed by a larger length field. The described invariant is that Commissioner Dataset TLVs in MGMT_COMM_SET handling must reject extended TLV length where the destination buffer expects bounded base TLVs.
