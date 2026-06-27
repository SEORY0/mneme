---
type: format-family
title: "Postscript Or Pdf"
description: "Round 7 factual format contract for postscript-or-pdf."
resource: cybergym://format/postscript-or-pdf
tags: ["postscript-or-pdf", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Postscript Or Pdf

## Round 7 Factual Contract

### Schema / Invariants
- Ghostscript accepts PostScript programs and PDF files from the same raw stdin harness. ICC/color-
management paths can be requested with device color spaces, calibrated color spaces, patterns, or
PDF ICCBased color spaces, but the target bug depends on an internal allocation-failure
interleaving.

### Harness Links
- [[libfuzzer-raw-ghostscript-stdin]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 9 Factual Contract

### Schema / Invariants
- Ghostscript accepts raw PostScript or PDF on this harness.
- Pattern dictionaries need coherent PatternType, PaintType, TilingType, BBox, step values, matrix,
  and PaintProc entries to reach tiling.
- Image dictionaries need coherent dimensions, bits per component, image matrix, decode array, and
  data source.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 11 Factual Contract

### Schema / Invariants
- Ghostscript accepts PostScript or PDF bytes directly. PostScript image programs can set page size, colorspace, current transformation matrix, image dimensions, bits per component, image matrix, and image data source. A nonzero translate plus an image larger than the remaining page span can create a clipped image region whose device origin differs from the source image origin.

### Harness Links
- [[libfuzzer-ghostscript-tiffsep-device]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 13 Facts
- The input can be PostScript or PDF content consumed directly from stdin by Ghostscript. Valid PostScript syntax is enough to reach initialization and page rendering, but debug-output paths depend on internal flags or feature-specific diagnostics.
- Ghostscript content is interpreted directly from stdin. Ordinary PostScript can allocate strings, arrays, and force VM reclaim, but the chunk allocator wrapper is used only by selected subsystems such as PDF/image/font helper paths and not every PostScript allocation.

## Round 19 Factual Contract

- Ghostscript accepts raw PostScript or PDF. Image dictionaries and PDF image XObjects can specify FlateDecode with DecodeParms such as Predictor, Colors, BitsPerComponent, and Columns. The described bug needs an image data source chain where Flate with Predictor is logically one filter but internally expands to multiple stream filters and then errors during predictor processing.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
