---
type: format-family
title: "Php Serialize format"
description: "Round 28 descriptive format facts for php-serialize."
resource: cybergym://format/php-serialize
tags: ["php-serialize", "round-28"]
okf_support: 0
---
# Php Serialize Format

## Round 28 Factual Contract

### Schema / Invariants
- PHP serialize wire values include objects, arrays, object references, and reference wrappers. SPL containers that implement Serializable use custom C records with a storage section and a members section; SplObjectStorage records contain an object entry and optional associated info value, followed by serialized object properties. Object-reference opcodes and regular reference opcodes are distinct: object references target objects, while reference wrappers can target arrays or other zvals. Internal classes that implement Serializable should use the custom-object form for their internal storage rather than plain object properties.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- PHP serialized values include custom Serializable objects, object values, arrays, and object-reference opcodes.
- SplObjectStorage custom serialization uses a storage section with an object count and object entries, optional associated info values, followed by a members section containing serialized object properties.
- Reference ids are resolved through the unserializer reference table and object references require the target to be an object.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
