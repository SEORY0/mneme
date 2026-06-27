---
type: format
title: "Haproxy Config"
input_format: haproxy-config
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Haproxy Config

## Schema
- HAProxy config parsing tokenizes one logical line into an output buffer plus an args array. Quoting, backslash escaping, comments, and environment expansion are handled before keyword dispatch; too many logical words are reported after output-buffer sizing has succeeded.
