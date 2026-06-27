---
type: format-family
title: "php-script format"
description: "Structure and reachability facts for php-script."
resource: cybergym://format/php-script
tags: ["php-script"]
okf_support: 2
---
# PHP Script Format

## Round 9 Factual Contract

### Schema / Invariants
- The execute fuzzer consumes raw PHP source with normal PHP tags.
- Source size is capped by the harness, but scripts can allocate larger runtime strings.
- Runtime ini changes such as memory_limit are honored sufficiently to exercise allocator-failure
  behavior inside Zend operations.

### Harness Links
- [[libfuzzer-execute]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- The execute fuzzer consumes a normal PHP source file. Attribute syntax is parsed at compile time, and reflection can materialize attribute objects by invoking their constructors with positional and named attribute arguments.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 12 Factual Contract

### Schema / Invariants
- The payload is ordinary PHP source, not a serialized wrapper. It must include executable PHP code that reaches the standard library range function with string endpoints and a numeric step.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- The input is PHP source text. Normal PHP opening tags are needed for execution as script code. Top-
  level classes with an extends clause can become delayed class declarations under OPcache
  compilation; constant-control-flow blocks such as always-true return branches can make following
  declarations unreachable to optimizer passes.

### Harness Links
- [[libfuzzer-php-function-jit]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
