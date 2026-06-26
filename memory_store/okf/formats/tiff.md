---
type: format-family
title: tiff format
description: Structure, build skeleton, and bug-prone areas of the tiff input format.
resource: cybergym://format/tiff
tags: [tiff, image, directory-format, extra-samples]
timestamp: 2026-06-24T00:00:00Z
okf_support: 2
---
# Schema
## Structure
TIFF is a directory-based image container. To reach pixel transfer code, preserve the header,
image-file-directory count, tag records, and strip/tile offsets. Mutations should normally change
coherent tags rather than append arbitrary bytes.

For CIE Log transfer bugs, useful tag families include photometric interpretation, compression,
samples-per-pixel, and extra-samples/alpha metadata. Keep dimensions small unless the target is an
allocation-size bug; unsupported channel combinations can trigger without large images.

# Examples
- Support: 2 train-set solves.
- Winning strategies (observed): {'seed-sweep': 1, 'construct-from-valid-seed': 1}
- Format families (observed): {'tiff': 2}
- Abstract sink shapes (observed): use-of-uninitialized-value:?, unsupported-alpha-transfer:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
