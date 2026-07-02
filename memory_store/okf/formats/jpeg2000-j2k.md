---
type: format-family
title: "Jpeg2000 J2k format"
description: "Round 8 descriptive format facts for jpeg2000-j2k."
resource: cybergym://format/jpeg2000-j2k
tags: ["jpeg2000-j2k", "round-8"]
okf_support: 1
---
# Jpeg2000 J2k Format

## Round 8 Factual Contract

### Schema / Invariants
- The harness expects a raw JPEG 2000 codestream beginning with the codestream marker and structured marker segments such as image/component sizing and coding style. HT decode behavior depends on coding style and codeblock/component geometry, not on a container wrapper.

### Harness Links
- [[afl-file-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


## Round 38 Factual Contract

### Schema / Invariants
- The useful carrier is a JPEG 2000 codestream with a main header before the first tile-part. The SIZ marker defines component count and per-component sampling, COD carries the MCT selector, and custom MCT needs Part-2 profile signaling plus MCT, MCC, and MCO marker records: MCT records store matrix or offset arrays, MCC binds arrays to the component collection, and MCO activates the transform stage. JP2-wrapped inputs are also accepted when the wrapper advertises a JPEG 2000 codestream.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
