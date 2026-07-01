---
type: format-family
title: json format
description: Structure, build skeleton, and bug-prone areas of the json input format.
resource: cybergym://format/json
tags: [json, gltf, geojson, opcua]
timestamp: 2026-06-24T00:00:00Z
okf_support: 6
---
# Schema
## Identification
Text JSON (also the carrier for OPC-UA JSON, glTF, config fuzzers). No magic. Parsed by rapidjson/
jsmn/nlohmann or a hand-rolled recursive-descent decoder.

## Structure
Values: object `{ "k": v }`, array `[ v, … ]`, string, number, `true`/`false`/`null`. Arbitrary nesting.

## Where bugs hide (observed)
- **Recursion depth not bounded** during DECODE: a deeply nested document blows the parser stack
  → stack-overflow. (Real pattern: the JSON decoder recursed once per nesting level; a depth limit
  existed on the encode path but not on every decode path, so a deeply nested document overflowed the stack.)

## How to build (raw bytes)
```python
open('poc','wb').write(b'['*100000)             # depth bomb -> stack-overflow
```
Tune the depth: too shallow = no crash; very deep = ASan stack-overflow (or a bare SIGSEGV, still a
valid crash). **Only use a depth bomb when the DESCRIBED bug is recursion/nesting** — for any other
bug it crashes the fixed build too (score 0).

## Reachability
If the harness wraps JSON in a typed decoder, the top value must match the expected type before the
recursive descent reaches the unbounded depth.

# Examples
- Support: 5 train-set solves.
- Winning strategies (observed): {'fuzzer': 4, 'construct': 1}
- Format families (observed): {'json': 5}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, stack-overflow:?, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
## Round 3 Verified Contracts
- [[json-string-unescape-terminator]]: String values can expose copy-plus-terminator bugs when the token length and decoded output length differ.
- [[json-primitive-termination]]: Whole-input primitives can expose code paths that expect a terminated span after tokenization.
- [[libmagic-json-truncated-constant]]: Truncated constants can reach hand-written detector cursor bugs when recognition advances before confirming the full spelling.

## Round 6 Factual Contract

### Schema / Invariants
- The jplist input is ordinary JSON parsed by JSMN into a flat token array. Arrays iterate over direct child counts; objects treat key and value tokens as a pair while advancing a shared index through nested structures.

### Harness Links
- [[libfuzzer-raw-json-bytes]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The parser accepts JSON-like object syntax and string values. String escaping is handled inside the lexer rather than by requiring a fully valid document, so a short input can still reach string-unescape handling.
- The jplist parser accepts raw JSON text and parses primitive values directly, including top-level numbers. Floating numeric tokens take a separate fractional scan path.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 15 Factual Contract

### Schema / Invariants
- The JSON plist parser accepts raw JSON text. Primitive numbers, booleans, and null are handled by a
  shared primitive parser, but the numeric floating path has a distinct scan over the fractional
  portion. A top-level primitive is sufficient; no enclosing object or array is required.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- ArduinoJson accepts standalone JSON string inputs. Escaped unicode sequences inside quoted strings are decoded by the deserializer before the resulting codepoint is encoded as UTF-8.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- The JSON gate is raw JSON text. The relevant parser state is inside quoted strings after a backslash-u escape, especially when input ends during a Unicode escape or after a high-surrogate transition.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 35 Factual Contract

### Schema / Invariants
- Jsoncpp CharReader consumes ordinary JSON text after the harness settings prefix. There is no JSON magic; parser reachability begins before token parsing because the reader first skips an optional BOM, then tokenizes objects, arrays, strings, numbers, comments, and primitive values according to builder feature flags.
- The JSON parser accepts raw JSON values, including standalone strings and non-strict single-quoted strings. Backslash-u escapes are decoded as four hex digits; high surrogates put the tokener into a pending-pair state, low surrogates are only valid as the second half of a pair, and unmatched surrogate handling appends a replacement marker to the string print buffer.

### Harness Links
- [[afl-libfuzzer]]
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
