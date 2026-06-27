---
type: format
title: "Git Smart Protocol"
input_format: git-smart-protocol
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Git Smart Protocol

## Schema
- The input is a Git smart transport byte stream made of pkt-lines, flush packets, ref advertisements, negotiation responses, and optional pack or sideband data. Pkt-lines use a length-prefixed ASCII envelope, and valid advertisements are needed before fetch negotiation and pack download paths run.
