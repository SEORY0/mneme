---
type: format-family
title: "html-fuzzer-input format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/html-fuzzer-input"
tags: ["html-fuzzer-input", "round-35"]
okf_support: 1
train_only: true
---
# html-fuzzer-input Format

## Round 35 Factual Contract
### Schema / Invariants
- The useful input is not a standalone browser HTML file but the libxml2 HTML fuzzer envelope: parser options followed by HTML bytes. The HTML document can use normal tags, META charset declarations, DOCTYPE public/system literals, comments, and text nodes. Declaring a charset can switch the parser to an encoding handler, but invalid or truncated bytes alone were not sufficient in these attempts. Unterminated literals and long text exercise normal HTML recovery without producing the target sanitizer signal.

### Harness Links
- [[afl-libfuzzer-compat-html]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
