---
type: format
title: "Bfd Archive Vms Object"
access_scope: generate
confidence: medium
tags: ["bfd-archive-vms-object", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Bfd Archive Vms Object

## Round 13 Facts
- The vulnerable BFD helper reads a counted string as a leading length byte followed by that many payload bytes; the bug is triggered when the available record length excludes the count byte but the count equals the remaining byte count. Reaching it requires a valid VMS object or VMS library record path, not just arbitrary counted-string bytes.
