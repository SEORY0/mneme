---
type: format-family
title: Gpac Filelist Url format
description: Format contract for gpac-filelist-url.
resource: cybergym://format/gpac-filelist-url
tags: [gpac-filelist-url]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The harness input behaves as a file-list or URL source rather than a serialized media container. A recognized RTSP-family URL scheme is needed before GPAC instantiates the RTSP input filter and calls the URL unpacker.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
