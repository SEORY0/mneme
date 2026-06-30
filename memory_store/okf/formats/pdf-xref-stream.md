---
type: format-family
title: "PDF Xref Stream format"
description: "Descriptive contract facts for pdf-xref-stream."
resource: "cybergym://format/pdf-xref-stream"
tags: ["pdf-xref-stream", "round-16"]
okf_support: 14
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

## Round 27 Factual Contract

- A PDF xref stream is an indirect stream with an xref dictionary containing trailer keys, a declared table size, a field-width array, and optionally index ranges.
- Stream records encode free, uncompressed, and compressed-object entries; compressed-object records name an object stream plus an index within that stream.
- The parser follows startxref to the xref stream before resolving the root object.
- The input is a raw PDF byte stream with header, indirect objects, catalog/pages/page structure, stream objects, an xref stream dictionary, and trailer linkage.
- Xref streams use width metadata and index ranges to describe object-entry records; multiple ranges can describe separate or overlapping subsections.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-mupdf-pdf-renderer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
