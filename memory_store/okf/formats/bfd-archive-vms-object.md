---
type: format
title: "Bfd Archive Vms Object"
input_format: bfd-archive-vms-object
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Bfd Archive Vms Object

## Schema
- The vulnerable BFD helper reads a counted string as a leading length byte followed by that many payload bytes; the bug is triggered when the available record length excludes the count byte but the count equals the remaining byte count. Reaching it requires a valid VMS object or VMS library record path, not just arbitrary counted-string bytes.
