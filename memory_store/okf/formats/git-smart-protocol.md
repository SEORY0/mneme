---
type: format
title: "Git Smart Protocol"
access_scope: generate
confidence: medium
tags: ["git-smart-protocol", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Git Smart Protocol

## Round 13 Facts
- The input is a Git smart transport byte stream made of pkt-lines, flush packets, ref advertisements, negotiation responses, and optional pack or sideband data. Pkt-lines use a length-prefixed ASCII envelope, and valid advertisements are needed before fetch negotiation and pack download paths run.
