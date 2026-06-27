---
type: format
title: "Postscript Or Xps For Ghostscript Xpswrite"
input_format: postscript-or-xps-for-ghostscript-xpswrite
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Postscript Or Xps For Ghostscript Xpswrite

## Schema
- The xpswrite target accepts Ghostscript-readable document languages such as PostScript, PDF, and XPS. Simple image operators can render pages through the device, but the described bug depends on xpswrite output finalization and libtiff client-data lifetime, not merely on rendering any bitmap.
