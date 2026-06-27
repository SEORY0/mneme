---
type: format-family
title: Javascript format
description: Structure and bug-prone gates for JavaScript program inputs.
resource: cybergym://format/javascript
tags: [javascript, construct, undefined-behavior-invalid-downcast]
okf_support: 1
---
# Schema
## Structure
For VM-construction downcast bugs, a syntactically valid program is enough to enter parsing
and interpreter setup. The trigger is the object construction path and derived-object
invariant, not a lexical edge case.

## Round 5 Verified Contracts
- [[javascript-global-object-downcast]]: Use any syntactically valid JavaScript program so the fuzzer proceeds from parsing into VM
creation. The interpreter construction path instantiates the global object, violating the
object-construction invariant by downcasting a base object during GlobalObject setup before
the derived object is valid.

# Examples
- Support: 1 server-verified solve.
- Winning strategies observed: construct.
- Abstract sink shape observed: undefined-behavior-invalid-downcast.

# Citations
- Distilled from server-verified training outcomes with this format family.

## Round 7 Factual Contract

### Schema / Invariants
- The input is JavaScript source text. String literals are delimited by single or double quotes; the
lexer also treats ECMAScript line-separator and paragraph-separator byte sequences as line
terminators.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 9 Factual Contract

### Schema / Invariants
- The input format is plain JavaScript source.
- RegExp literals and RegExp constructor calls are parsed and compiled by Hermes before execution;
  JavaScript exceptions are swallowed by the harness.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input is plain JavaScript source. The relevant language feature is RegExp.prototype[Symbol.split] over strings whose byte length differs from character length, especially when the regular expression is made sticky and repeated matches update lastIndex.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
