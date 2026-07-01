---
type: format-family
title: mruby-source format
description: Format contract for mruby-source.
resource: cybergym://format/mruby-source
tags: [mruby-source, "round-16"]
okf_support: 7
train_only: true
---
# Schema
## Structure
Inputs follow the `mruby-source` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The input is plain mruby source text. Big integer literals and arithmetic are parsed or executed by
  mruby and can allocate RBigint objects whose internal limb array has a sign, size, and pointer. Most
  arithmetic return paths normalize zero back to a fixnum, avoiding the vulnerable zero-length Bigint
  state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- The input is ordinary mruby source text. Relevant syntax families include loops, rescue/ensure blocks, lambda return behavior, boolean short-circuit operators, and jump-like statements such as break, next, redo, and return.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- The input is ordinary mruby source text. Sprintf format strings are interpreted at runtime; numeric width and precision fields are parsed from decimal text before the C implementation casts them for internal formatting arithmetic.

### Harness Links
- [[libfuzzer-raw-mruby-source]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 19 Factual Contract

- The input is plain mruby source code. Useful candidates must be syntactically valid Ruby and reach compiler/codegen behavior rather than binary parsing. Block forms with ordinary arguments, splats, destructuring, defaults, nested lambdas, and block forwarding are accepted language constructs.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The input is Ruby source code. String#index and String#split with a string separator reach mruby's byte-string search helper when both haystack and needle lengths are large enough for the quick-search branch.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- The input is plain mruby source text. Runtime array bugs require syntactically valid code that reaches Array assignment/splice operations rather than bytecode or a secondary container.
- The format is plain mruby source text. Integer literals exceeding the immediate range become heap-backed bigint objects; generic Object#dup and Object#clone can be invoked directly on those values.

### Harness Links
- [[honggfuzz-file]]
- [[libfuzzer-mruby-load-string]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- The input is ordinary mruby source text. sprintf format strings are parsed at runtime; width and precision can be literal decimal fields or supplied by star arguments. Float conversions flow through the mruby sprintf implementation into floating-point formatting helpers.
- The input is raw mruby source code. The relevant sink family is floating-point formatting via Ruby formatting calls, where format-string width or precision values flow into the C float formatting helper.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-raw-mruby-source]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Schema / Invariants
- The input is plain mruby source text. Parser reachability depends on valid Ruby syntax; integer literals outside the compact immediate ranges are emitted through wider integer opcodes during code generation. Method bodies and local assignments are useful carriers because they create temporary registers and later local moves that can trigger peephole rewrites.

### Harness Links
- [[libfuzzer-mruby-load-string]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- The input is plain mruby source text. Destructured block or method parameters can create unnamed local-variable slots in compiled instruction records. The vulnerable conversion is in the symbol-name rendering path used by verbose instruction/local-variable dumps; ordinary source execution and most runtime reflection methods do not dump every local slot.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 31 Factual Contract

### Schema / Invariants
- The input is plain mruby source text. Parser reachability depends on valid Ruby syntax; string literals can be evaluated by the VM, and String#to_f or equivalent Float conversion routes numeric string contents through the shared string-length-to-double helper. Numeric text, optional whitespace, underscores between digits, hexadecimal prefixes, and embedded NULs are handled by that helper before native float parsing.

### Harness Links
- [[libfuzzer-mruby-load-string]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- The input is plain mruby source text. It must be syntactically valid Ruby that executes under mrb_load_string. Heap-backed strings are needed for shared-string behavior; substring or slice operations over a non-embedded string can create a shared string object that aliases the original backing storage.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- The input is plain mruby source text. Destructured block and method parameters can create unnamed local-variable slots, but ordinary runtime reflection such as parameter and local-variable enumeration filters those slots before symbol conversion. Source-location pseudo values are handled during parsing/code generation and can reach filename-symbol conversion without needing runtime reflection or the CLI verbose dump path.

### Harness Links
- [[libfuzzer-mruby-load-string]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
