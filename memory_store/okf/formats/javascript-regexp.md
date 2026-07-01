---
type: format-family
title: "Javascript Regexp"
description: "Round 36 factual format contract for javascript-regexp."
tags: ["javascript-regexp", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Javascript Regexp

## Round 36 Factual Contract

### Schema / Invariants
- The relevant input language is JavaScript source evaluated by Hermes. RegExp constructor patterns are JS strings that the regex parser consumes as a UTF-style pattern stream. Escapes in the pattern are interpreted by the regex parser after JavaScript string construction, so a generated string can end with a single regex escape character without relying on an invalid JavaScript literal.

### Harness Links
- [[libfuzzer-raw-js]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
