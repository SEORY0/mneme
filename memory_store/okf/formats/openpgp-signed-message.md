---
type: format
title: "Openpgp Signed Message"
input_format: "openpgp signed message"
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Openpgp Signed Message

## Schema
- OpenPGP signed-message inputs must preserve packet framing well enough for GPG verification to parse literal/plaintext content under a signature. Signed and clearsigned repository samples reached the plaintext handler; encrypted-message samples did not exercise the same verification path.
