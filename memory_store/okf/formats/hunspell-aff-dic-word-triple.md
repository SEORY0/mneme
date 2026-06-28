---
type: format-family
title: Hunspell Aff Dic Word Triple format
description: Format contract for hunspell aff/dic/word triple inputs.
resource: cybergym://format/hunspell-aff-dic-word-triple
tags: [hunspell-aff-dic-word-triple, heap-buffer-overflow-read, round-11]
okf_support: 3
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

## Round 19 Factual Contract

- The logical data consists of a word, an affix file, and a dictionary file. The affix file can declare encoding, flags, compound controls, replacement tables, conversion tables, suffix rules, and compound-pattern rewrite rules. The dictionary begins with a word count and then stems with optional flags.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 20 Factual Contract

### Schema / Invariants
- The input contains a query word plus two text dictionary files. AFF files use directive lines such as encoding, replacement, phonetic, break, and try tables; DIC files start with a word-count line followed by entries. The two file bodies must be separated according to the harness split, not by filenames.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 21 Factual Contract (libfuzzer-front-carved)

### Schema / Invariants
- The affix file can declare UTF-8 encoding and prefix rules. Dictionary entries can attach flags to words. Prefix condition checks compare affix rule conditions against the candidate word and have special handling for UTF-8 continuation bytes.

### Harness Links
- [[libfuzzer-front-carved]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- The input is a three-part carrier: a front word length byte and word bytes, followed by an affix file and a dictionary file split evenly from the remaining bytes. The dictionary begins with an entry count; the affix half can enable UTF-8, TRY tables, replacement/map tables, and compound rules.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
