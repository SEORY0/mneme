---
type: format
title: "Postscript Or Pdf"
input_format: postscript-or-pdf
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Postscript Or Pdf

## Schema
- The input can be PostScript or PDF content consumed directly from stdin by Ghostscript. Valid PostScript syntax is enough to reach initialization and page rendering, but debug-output paths depend on internal flags or feature-specific diagnostics.
- Ghostscript content is interpreted directly from stdin. Ordinary PostScript can allocate strings, arrays, and force VM reclaim, but the chunk allocator wrapper is used only by selected subsystems such as PDF/image/font helper paths and not every PostScript allocation.
