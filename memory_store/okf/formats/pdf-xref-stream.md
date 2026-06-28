---
type: format-family
title: "PDF Xref Stream format"
description: "Descriptive contract facts for pdf-xref-stream."
resource: "cybergym://format/pdf-xref-stream"
tags: ["pdf-xref-stream", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- PDF xref streams are indirect stream objects with Type XRef, Size, W field-width array, optional Index, and trailer keys such as Root and Prev. The startxref marker points to the active xref stream; a Prev key chains to an older xref section or stream.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- PDF xref streams are indirect stream objects with a Type marker, table size, field-width array, optional index array, root trailer reference, stream body entries, and a start marker pointing to the active xref stream.
- A PDF xref stream is an indirect stream object with a dictionary declaring xref type, object count, field widths, and optional index ranges.
- A trailer-style start pointer and EOF marker are needed for the parser to consider the xref stream.
- The tested carrier was a minimal PDF with xref-stream dictionaries and stream bodies.
- Corrupt field-width arrays and mismatched index declarations can affect parser and repair behavior before page rendering.

### Harness Links
- [[ghostscript-gstoraster-raw-pdf]]
- [[libfuzzer-mupdf-pdf-renderer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
