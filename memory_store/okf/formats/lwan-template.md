---
type: format-family
title: "Lwan Template format"
description: "Structure and invariants for the lwan-template input format."
tags: ["lwan-template", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Lwan templates use mustache-like tags for escaped variables, unescaped variables, sections, inverted sections, and partial/template references. Variable names must match the descriptor table supplied by the harness; unknown or overlong lexemes are parser errors rather than expansion-time data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 34 Factual Contract

### Schema / Invariants
- Lwan templates are Mustache-like text. Actions use double braces; variables must match the harness descriptor table. Conditional sections use a question suffix and close with the same name plus the question suffix. Sequence sections use a hash marker and close by name. Inverted sections use a caret before a variable or before a hash section. Partials use a greater-than marker followed by an identifier-like path. Parser errors are common for unknown variables, unmatched sections, malformed close markers, and invalid triple-brace escaping.
- Lwan templates use Mustache-like markers for variables, unescaped variables, sections, inverted sections, comments, and partials. Parser-visible identifiers are matched against a descriptor table, and malformed or unknown tags can be rejected cleanly. For this task the decisive invariant was the harness pre-parser copy and terminator behavior, not a template grammar invariant.
- Lwan template input is plain text using Mustache-like delimiters. The parser accepts variables, escaped variables, conditional sections, inverted sections, sequence sections, inverted sequence sections, comments, and partial references. Names must be present in the descriptor table active for the current section. Parser-balanced section tags can still create post-processing chunk relations involving start, end, and last chunks.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
