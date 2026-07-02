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

## Round 23 Factual Contract

### Schema / Invariants
- The fuzzer input is split at a separator. Bytes before the separator become the data passed to hash_update, and bytes after the separator are a PHP serialized value. HashContext unserialization expects an array-like payload with algorithm, options, internal hash state, magic value, and object members.

### Harness Links
- [[libfuzzer-directory-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- The input is split at the first separator into an update string and a PHP serialized value.
- The serialized value must instantiate a HashContext object.
- HashContext::__unserialize expects a five-field array: algorithm string, options integer, algorithm-specific serialized state, a magic/layout integer, and object members.
- For xxh64 the algorithm-specific state is a generic spec array of serialized 32-bit words representing 64-bit state words plus 32-bit counters; the internal small-buffer occupancy counter must remain below the xxhash block-buffer capacity.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
