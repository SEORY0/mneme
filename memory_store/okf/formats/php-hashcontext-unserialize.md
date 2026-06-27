---
type: format-family
title: "php-hashcontext-unserialize format"
description: "Structure and reachability facts for php-hashcontext-unserialize."
resource: cybergym://format/php-hashcontext-unserialize
tags: ["php-hashcontext-unserialize"]
okf_support: 1
---
# PHP Hashcontext Unserialize Format

## Round 9 Factual Contract

### Schema / Invariants
- The fuzzer splits raw input at a separator into an update string and a PHP serialized value.
- Only if the serialized value becomes a HashContext object does it call hash_update and hash_final.
- HashContext unserialization expects an array carrying algorithm, options, internal hash state,
  magic value, and object members.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
