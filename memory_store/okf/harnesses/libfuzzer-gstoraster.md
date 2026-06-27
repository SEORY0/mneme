---
type: harness
title: "Libfuzzer Gstoraster"
harness_convention: libfuzzer-gstoraster
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Gstoraster

## Input Contract
- For `postscript-or-pdf`, The gstoraster harness passes the raw input bytes through Ghostscript stdin with cups output-device arguments, quiet/batch/no-pause flags, and no leading mode selector or FuzzedDataProvider carving.
- For `postscript-or-pdf`, The harness is the same raw gstoraster libFuzzer target as other Ghostscript tasks: no input prefix, no external file dependencies, and Ghostscript is invoked with fixed cups rasterization arguments.
