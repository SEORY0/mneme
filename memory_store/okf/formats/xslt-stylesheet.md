---
type: format-family
title: Xslt Stylesheet format
description: Format contract for xslt stylesheet inputs.
resource: cybergym://format/xslt-stylesheet
tags: [xslt-stylesheet, double-free, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The target input is a standalone XSLT stylesheet document. The XML parser accepts internal DTD entity declarations and XSLT top-level/template/variable content; entity references can appear in template bodies or stylesheet-level content, but ordinary internal entities may be expanded or ignored without creating the vulnerable ownership state.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- The input is raw XML/XSLT.
- An internal DTD can declare parsed entities, and without XML entity substitution the stylesheet tree can retain entity-reference nodes.
- Ordinary entity references in top-level, template, variable, literal-result, or text-only carriers can parse and transform cleanly; the crashing shape requires the entity reference to survive into an executed template context that evaluates message content with nested attribute construction.

### Harness Links
- [[afl-file-xslt]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
