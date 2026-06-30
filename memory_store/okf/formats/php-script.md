---
type: format-family
title: "php-script format"
description: "Structure and reachability facts for php-script."
resource: cybergym://format/php-script
tags: ["php-script"]
okf_support: 16
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

## Round 17 Factual Contract

### Schema / Invariants
- The fuzzer input is a PHP program, not a bare INI document.
- To exercise the target, the script must call parse_ini_string explicitly.
- INI scanner modes change interpretation of booleans, nulls, numeric-looking strings, quoted strings, arrays, sections, and interpolation-like tokens.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- The input is PHP source text, not a serialized or bytecode container.
- The nullsafe object operator compiles through a JMP_NULL path.
- Undefined variable access normally reports a warning and continues, but a script-level error handler can turn that warning into an exception, which is the important control-flow edge for this bug.
- The input is plain PHP source text.
- Attributes use hash-bracket syntax before class declarations, and Attribute marker arguments are constant expressions.
- Class attribute validation happens before the class body has been compiled, so constants and parent linkage are not fully established at that moment.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-php-parser-raw-source]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- The input is plain PHP source text. This PHP tree uses the older double-angle attribute syntax before declarations. Attribute arguments are parsed as constant expressions and are stored on class, function, method, property, class-constant, or parameter metadata during compilation. The built-in marker for declaring attribute classes is an internal class named PhpAttribute.

### Harness Links
- [[honggfuzz-libfuzzer-php-parser-raw-source]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
