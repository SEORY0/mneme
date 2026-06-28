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

