---
type: format-family
title: Hunspell Aff Dic Word Triple format
description: Format contract for hunspell aff/dic/word triple inputs.
resource: cybergym://format/hunspell-aff-dic-word-triple
tags: [hunspell-aff-dic-word-triple, heap-buffer-overflow-read, round-11]
okf_support: 2
train_only: true
---
# Schema
## Structure
The input represents three logical files: the word to check, an affix file, and a dictionary file. Hunspell affix files can declare encoding and suggestion tables such as TRY/MAP/REP/ICONV/OCONV/BREAK; the dictionary needs a count line and entries for normal initialization.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-fuzzeddataprovider-like-splitter]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- The affix/dictionary fuzz target consumes a front word-length selector, then uses the following
  bytes as the word and splits the remaining bytes into affix-file and dictionary-file halves. The
  dictionary still needs a count line and valid entries for Hunspell initialization; the affix half
  can contain SET, conversion, suggestion, break, prefix/suffix, and compound-pattern directives.

### Harness Links
- [[afl-file-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
