---
type: format-family
title: ILBM image format
description: Format contract for IFF-style ILBM chunk streams and bitmap headers.
resource: cybergym://format/ilbm
tags: [ilbm, iff, chunked-image, bitmap-header]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
ILBM uses an IFF-style form with typed chunks. Bitmap-header decoder bugs require a valid form selector and a bitmap-header chunk that is reached by the loader.

## Invariants
- Keep outer form and chunk walking valid.
- Short fixed-structure chunk payloads can trigger overreads.
- Do not remove the bitmap-header chunk while minimizing.
