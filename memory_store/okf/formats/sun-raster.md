---
type: format
title: "Sun Raster"
input_format: sun-raster
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Sun Raster

## Schema
- SUN raster input starts with a fixed big-endian raster header containing magic, dimensions, bit depth, data length, raster type, colormap type, and colormap byte length. Indexed images below truecolor depth can carry either an implicit colormap or three equal-length color planes for red, green, and blue. Pixel rows are padded to an even byte boundary; encoded rasters use a simple byte-run scheme that must expand to the expected raster extent.
