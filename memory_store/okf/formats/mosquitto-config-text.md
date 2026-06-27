---
type: format
title: "Mosquitto Config Text"
input_format: mosquitto-config-text
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Mosquitto Config Text

## Schema
- Mosquitto broker configuration is newline-separated directive text. Some global directives implicitly create or modify the default listener, while explicit listener directives append listener records to the listener array. Directives are processed sequentially and later directives operate on parser state created by earlier lines.
