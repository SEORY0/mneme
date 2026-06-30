---
type: format-family
title: "Url String format"
description: "Round 28 descriptive format facts for url-string."
resource: cybergym://format/url-string
tags: ["url-string", "round-28"]
okf_support: 0
---
# Url String Format

## Round 28 Factual Contract

### Schema / Invariants
- The URL fuzzer accepts a raw URL byte string with no container header, checksum, or length fields. A special-scheme URL with authority reaches host and path states; path bytes are consumed through Utf8View, so malformed UTF-8 in the path is dereferenced by Utf8CodePointIterator before URL percent-encoding or path finalization.

### Harness Links
- [[libfuzzer-raw-bytes]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
