---
type: format-family
title: "Pdf Or Postscript"
description: "Round 7 factual format contract for pdf-or-postscript."
resource: cybergym://format/pdf-or-postscript
tags: ["pdf-or-postscript", "format-contract", "round-7"]
okf_support: 11
train_only: true
---
# Pdf Or Postscript

## Round 7 Factual Contract

### Schema / Invariants
- PDF text rendering mode is set in page content streams and mode 3 makes text invisible while still
exercising text show operations. Related clipping modes and stringwidth paths can also use a null
device internally.

### Harness Links
- [[libfuzzer-raw-ghostscript-stdin]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- The relevant structure is a PDF font ToUnicode CMap or equivalent PostScript CMap with codespace and bfchar/bfrange entries. Malformed range arrays can be syntactically accepted while leaving the conversion logic with inconsistent range cardinality.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Schema / Invariants
- Ghostscript accepts raw PostScript jobs and complete PDF documents. Useful PDF carriers need a catalog, pages tree, page, resources, content stream, and renderable operators. Spot-color state can be introduced through PDF Separation color spaces in page resources, through PostScript setpagedevice SeparationColorNames, PageSpotColors, MaxSeparations, and SeparationOrder, or through PDF page scanning that writes SeparationColorNames and PageSpotColors to the device. Transfer functions can be supplied by PostScript settransfer or setcolortransfer, or by PDF ExtGState transfer entries.

### Harness Links
- [[libfuzzer-ghostscript-psdcmyk]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- Ghostscript accepts raw PostScript programs and complete PDF documents.
- Renderable PDFs need a header, catalog, pages tree, page, media box, resources, content stream, cross-reference data, trailer, and end marker.
- PDF image XObjects, ExtGState alpha, soft masks, and form XObjects with transparency groups can force rendering and pdf14 compositor setup.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
