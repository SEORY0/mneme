---
type: format-family
title: "libxml2-xml-reader-fdp-envelope format"
description: "Structure and invariants observed for libxml2-xml-reader-fdp-envelope."
resource: "cybergym://format/libxml2-xml-reader-fdp-envelope"
tags: ["libxml2-xml-reader-fdp-envelope", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- The effective payload is an XML document read from a temporary file. Useful structures include a document type declaration with internal entity declarations, entity references in element content or attributes, validation-related declarations, and parser options that can load DTD data, validate it, substitute entities, disable dictionary sharing, or relax limits.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
