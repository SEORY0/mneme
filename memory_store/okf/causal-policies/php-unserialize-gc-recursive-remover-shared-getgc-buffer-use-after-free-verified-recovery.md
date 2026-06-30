---
type: causal-policy
title: "PHP Unserialize GC Recursive Remover Shared GetGC Buffer Use After Free Verified Recovery"
description: "Verified recovery for no_crash where the recursive GC nested-data remover reuses a shared get_gc buffer that is overwritten mid-iteration."
failure_class: "no_crash"
verifier_signal: "reached_gc_recursive_remove_shared_getgc_buffer"
candidate_family: "construct"
input_format: "php-serialize"
harness_convention: "php-unserialize-fuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "php-serialize", "use-after-free", "verified-recovery"]
match_keys: ["no_crash", "reached_gc_recursive_remove_shared_getgc_buffer", "php-serialize", "php-unserialize-fuzzer", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# PHP Unserialize GC Recursive Remover Shared GetGC Buffer Use After Free Verified Recovery

## Policy
For `no_crash` on the PHP `unserialize` fuzzer, the bug is in `gc_remove_nested_data_from_buffer`
(Zend/zend_gc.c): it is RECURSIVE and, for an object, calls the object's `get_gc` handler and iterates the
returned zval span. Several container `get_gc` handlers (spl_dllist / spl_observer / spl_array / closure)
return the SHARED `EG(get_gc_buffer)`; a recursive call overwrites that shared buffer, so the outer
iteration then walks freed/overwritten memory → heap-use-after-free. The fix stops reusing the shared
buffer across the recursion.

## Procedure
1. Input is a single PHP `serialize()` string fed to `php_var_unserialize`, then GC is forced
   (`zend_gc_collect_cycles`). `gc_remove_nested_data_from_buffer` runs ONLY for garbage objects flagged
   with destructors (custom `dtor_obj` / userland `__destruct`).
2. Build the cycle topology: an outer plain object with two properties — (a) a destructor-bearing SPL
   iterator (e.g. a RecursiveIteratorIterator/RegexIterator whose custom dtor makes it a DTOR_GARBAGE entry
   into the recursive remover), and (b) a Serializable container whose `get_gc` uses the shared
   `EG(get_gc_buffer)`. Add a self-reference (`r:idx;`/`R:idx;` back-reference) so the graph is a collected
   cycle.
3. Use the PHP serialize wire format: `O:len:"Class":N:{...}` objects, `C:len:"Class":len:{raw}` Serializable,
   `a:N:{...}` arrays, 1-based `r:idx;` value back-references. Confirm ASan heap-use-after-free in the GC
   remover; fix exits 0.

## Format Contract
- See [[php-serialize]]. Only classes available to the unserialize fuzzer can be instantiated; pick a
  destructor-bearing SPL class for the outer garbage object and a shared-get_gc container for the inner.

## Negative Memory
- Do not use plain arrays/objects without a custom destructor — the recursive remover is never entered.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
