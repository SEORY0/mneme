---
type: format-family
title: "Pdf Xref Stream With Object Stream Format"
description: "Input contract facts for pdf-xref-stream-with-object-stream."
tags: ["pdf-xref-stream-with-object-stream", "round-30"]
okf_support: 0
train_only: true
---
# Pdf Xref Stream With Object Stream Format

## Round 30 Factual Contract

### Schema / Invariants
- PDF xref streams encode object entries with width metadata and can mark an object as compressed inside an object stream. Object streams declare an object count and a First value; their stream data begins with object-number and relative-offset pairs followed by serialized objects. MuPDF uses those entries while resolving the page tree, so a page object stored in an object stream forces object-stream loading before rendering. Stream dictionaries carry /Length, but MuPDF's PDF stream wrapper can distrust that length and scan forward for endstream-like terminators.

### Harness Links
- [[libfuzzer-mupdf-pdf-renderer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
