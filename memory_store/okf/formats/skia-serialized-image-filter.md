---
type: format-family
title: "skia-serialized-image-filter format"
description: "Structure and reachability facts for skia-serialized-image-filter."
resource: cybergym://format/skia-serialized-image-filter
tags: ["skia-serialized-image-filter"]
okf_support: 1
---
# Skia Serialized Image Filter Format

## Round 9 Factual Contract

### Schema / Invariants
- The target format is Skia's internal flattened SkImageFilter serialization, not a PNG/JPEG/GIF
  image.
- A useful input must deserialize into an image filter object graph; to reach the described bug it
  likely needs a paint/shader branch containing a serialized picture shader and dimensions or tile
  state that force the EmptyShader path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
