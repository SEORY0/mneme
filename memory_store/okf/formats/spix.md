---
type: format-family
title: "Spix format"
description: "Round 8 descriptive format facts for spix."
resource: cybergym://format/spix
tags: ["spix", "round-8"]
okf_support: 1
---
# Spix Format

## Round 8 Factual Contract

### Schema / Invariants
- SPIX is Leptonica serialized PIX data with a recognizable file-type header followed by serialized image metadata and raster data. Common image formats such as JPEG are not accepted by pixReadMemSpix in this harness even though Leptonica can read them elsewhere.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- SPix is an uncompressed serialized PIX: an ASCII file id, image dimensions, depth, words-per-line metadata, optional colormap data, a raster byte count, and raw raster words. The deserializer recomputes the raster layout from dimensions and depth and requires the declared and actual raster sizes to agree.
- SPIX is a native word-oriented serialized Pix format with a magic word, dimensions, depth, word stride, optional color map entries, raster byte count, and raster words. Color map count must be compatible with image depth, and raster length must match the computed words-per-line times height.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- Serialized PIX inputs carry a magic/header region, native integer image fields, optional serialized colormap entries, a raster byte count, and raster data. Low-bit-depth colormapped images can be accepted even when sample values are not bounded by the number of colormap entries; grayscale versus color palette classification changes which enhancement path is reached.
- SPIX is Leptonica's uncompressed serialized PIX format. It begins with an ASCII file identifier stored in the word-oriented stream, followed by image width, height, depth, a serialized words-per-line field, a color-map count with optional color-map words, a raster byte-count field, and raw raster words. The deserializer recomputes the raster layout from width, height, and depth and requires the declared raster size and actual remaining raster size to match before constructing the PIX.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- SPIX is Leptonica's raw serialized Pix format.
- It starts with a short file identifier, native-width integer image fields for width, height, depth, word stride, color-map count, then optional color-map words, a raster-size word, and raw raster words.
- For 1bpp images, pixels are stored in 32-bit word rows, with the logical pixel order matching the library's high-bit-first bit accessors.
- The deserializer requires the advertised raster byte count, computed stride-by-height byte count, and actual remaining payload length to agree.
- SPIX is Leptonica's raw serialized PIX format.
- It starts with an ASCII identifier followed by native little-endian words for width, height, depth, raster words per line, colormap count, optional serialized colormap entries, raster byte count, and uncompressed raster words.
- The raster byte count must match both the dimensions/depth-derived stride and the remaining file length.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
