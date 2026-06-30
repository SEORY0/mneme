---
type: format-family
title: xml format
description: Structure, build skeleton, and bug-prone areas of the xml input format.
resource: cybergym://format/xml
tags: [xml]
timestamp: 2026-06-24T00:00:00Z
okf_support: 7
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 7 train-set solves.
- Winning strategies (observed): {'seed-sweep': 6, 'fuzzer': 1}
- Format families (observed): {'xml': 7}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
## Round 3 Verified Contracts
- [[xml-xinclude-fallback-namespace-uaf]]: XInclude fallback ownership bugs require the entity/envelope options and serialization path, not just malformed XML.

## Round 6 Factual Contract

### Schema / Invariants
- The XML typefinder requires at least a small minimum total length, searches for an opening tag, optionally recognizes an XML declaration, skips comments, and then checks the first element name for generic XML or specialized XML-derived formats.

### Harness Links
- [[libfuzzer-push-buffer-typefind-pipeline]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- The useful format is XML text with optional declarations, encodings, entities, and nested content that can drive libxml2 input-buffer growth and error handling. Merely malformed XML or entity expansion is insufficient without the allocation/reset timing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 13 Facts
- The target parser is libxml2's xmlTextReader path over an XML document containing DTD declarations, entity declarations, and possible entity-reference nodes. The vulnerable lifetime shape is tied to freeing document-level entity structures before freeing reader node lists that can still contain references.

## Round 17 Factual Contract

### Schema / Invariants
- libxml2 dictionaries intern element and attribute names in string pools.
- Fuzzing builds use a deterministic dictionary seed, so hash collisions can be generated offline.
- The risky comparison only occurs after hash equality and lookup into an occupied dictionary slot; ordinary non-colliding names never reach the memcmp path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 19 Factual Contract

- The useful structure is raw XML text with an internal DTD declaring an element and namespace declaration attributes. Namespace declarations can be written with a prefix or default xmlns name, and DTD attribute type/default choices control whether validation attempts ID handling on the namespace declaration.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Schema / Invariants
- The XML parser accepts an internal DTD subset before the document element. Element declarations and attribute-list declarations are processed during parsing, and default attributes are stored as grouped name/type/value metadata before being applied to the element.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
