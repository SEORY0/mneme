---
type: format-family
title: "Php Source format"
description: "Descriptive contract facts for php-source."
resource: "cybergym://format/php-source"
tags: ["php-source", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The input is PHP source text, not serialized PHP data.
- Property hooks are declared in class property syntax, lazy objects are created through ReflectionClass, and foreach over an object asks the object handler for an iterator over declared and dynamic properties.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 19 Factual Contract

- The input format is plain PHP source. Useful candidates are complete scripts that avoid parse errors and interpreter bailouts, then run repeated loops or function calls to make JIT traces hot. Global variable access, mutation of refcounted values, and binding/importing globals are the relevant language features for this bug class.
- Harness link: [[libfuzzer-tracing-jit]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 25 Factual Contract

### Schema / Invariants
- The input is PHP source text. Ordinary reserved words in identifier-capable grammar positions carry identifier metadata; the short echo opener can produce the same token kind without that metadata. Namespace import aliases, function names, class/member names, and trait alias constructs are candidate identifier contexts.
- The input is PHP source text. Recursive arrays can be created by assigning references into arrays and then passing the array by reference to the sort function. Regular PHP opening tags and statement syntax are required for the execute fuzzer.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
