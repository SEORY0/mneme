---
type: format-family
title: "Libxml2 Xml Reader Byte Stream format"
description: "Round 28 descriptive format facts for libxml2-xml-reader-byte-stream."
resource: cybergym://format/libxml2-xml-reader-byte-stream
tags: ["libxml2-xml-reader-byte-stream", "round-28"]
okf_support: 0
---
# Libxml2 Xml Reader Byte Stream Format

## Round 28 Factual Contract

### Schema / Invariants
- The effective input is not raw XML at file start. The harness consumes a little-endian parser-options integer, a size-prefixed encoding string, and a size-prefixed XML file-content string. XML element and attribute names are interned in the parser dictionary unless the no-dictionary option is selected. xmlTextReader can cache freed element and text nodes during traversal and later xmlSAX2StartElementNs can reuse those nodes for new elements.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
