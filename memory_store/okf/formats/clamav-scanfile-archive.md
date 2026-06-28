---
type: format-family
title: "clamav-scanfile-archive format"
description: "Structure and reachability facts for clamav-scanfile-archive."
resource: cybergym://format/clamav-scanfile-archive
tags: ["clamav-scanfile-archive"]
okf_support: 1
---
# Clamav Scanfile Archive Format

## Round 9 Factual Contract

### Schema / Invariants
- The scanner fuzzer writes the input bytes to a temporary file and enables broad ClamAV parsing
  options.
- The target bug is in EGG archive name/string conversion, so the input must be recognized as an
  archive member format that routes a name through the UTF-8 conversion helper.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
