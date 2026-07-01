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

## Round 28 Factual Contract

### Schema / Invariants
- The parser fuzzer consumes PHP source text and compiles it without executing normal application logic. The fuzzer SAPI starts a request with a hardcoded disabled-functions list, then shuts the request down, so source that redeclares names from that disabled set can affect the function table observed by shutdown cleanup.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The input is ordinary PHP source text, not PHPT sections or a binary container. A PHP opening tag is sufficient to enter parser mode. Top-level function declarations are registered during compilation even when the parser fuzzer does not execute userland code. Source must stay under the parser fuzzer size cap, but it can still contain many compact declarations.

### Harness Links
- [[libfuzzer-parser]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- The execute fuzzer compiles the uploaded bytes as a normal PHP file buffer, so executable source needs the PHP opening tag. The fuzzer limits the source size and replaces zend_execute_ex with a step counter that calls zend_bailout after the budget is exhausted. Fiber objects can be created from userland callbacks, started, suspended, and destroyed during request shutdown. User-defined destructors run at shutdown unless disabled by fatal-error handling.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
