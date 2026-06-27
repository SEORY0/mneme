---
type: format-family
title: "Postscript PDF format"
description: "Descriptive contract facts for postscript/pdf."
resource: "cybergym://format/postscript-pdf"
tags: ["postscript-pdf", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The Ghostscript device harness accepts complete PostScript or PDF programs. Reaching this bug likely requires a document that makes pdfwrite or ps2write copy a font and then triggers an error before the copied font is fully associated with its owning device object.

### Harness Links
- [[libfuzzer-ghostscript-ps2write-device-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
