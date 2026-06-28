---
type: format
title: "Openpgp Signed Message"
access_scope: generate
confidence: medium
tags: ["openpgp-signed-message", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Openpgp Signed Message

## Round 13 Facts
- OpenPGP signed-message inputs must preserve packet framing well enough for GPG verification to parse literal/plaintext content under a signature. Signed and clearsigned repository samples reached the plaintext handler; encrypted-message samples did not exercise the same verification path.
