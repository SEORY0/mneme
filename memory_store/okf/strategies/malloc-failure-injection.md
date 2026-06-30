---
type: strategy
title: malloc-failure-injection strategy
description: Trigger allocation-failure-handling bugs by driving the fuzzer's built-in OOM injector
resource: cybergym://strategy/malloc-failure-injection
tags: [malloc-failure-injection, oom-injection, maxalloc-sweep, libxml2, error-path]
timestamp: 2026-06-29T00:00:00Z
okf_support: 4
provenance: claude-precise-analysis-2026-06-29
---
## What
Many parser fuzzers (notably the libxml2 fuzz/ targets) ship an **allocation-failure injector**: the
input carries a `maxAlloc` field and the harness forces the *maxAlloc-th* allocation to return NULL.
Whole bug classes — "use of uninitialized value / buffer overread / use-after-free / NULL deref **in
cases of malloc failure**" — are ONLY reachable by driving this injector. Feeding plain well-formed
input never triggers them (the symptom looks like `no_crash`). The recovery is: apply the harness's OOM
header, reach the vulnerable function with the allocation **unlimited** first, then **sweep `maxAlloc`**
to fail the one allocation that the fix learned to handle.

## When
- Description says the bug occurs "**in cases of malloc failure**", "improper handling of memory
  allocation failures", "not reset/checked on error", or the diff adds an `XML_PARSER_EOF` /
  `errNo == XML_ERR_NO_MEMORY` / NULL-after-alloc guard on an error path.
- Local `verify` keeps returning `no_crash` on structurally-valid input that clearly reaches the parser.
- See harness contract [[libxml2-fuzzer-malloc-injection]].

## Steps
1. Read the named function AND diff vul-vs-fix (copy the fix source from the fix image, `diff`) to find
   the **exact added guard** and the value it protects (uninitialized length, freed/dangling pointer,
   NULL pop). That tells you *which* allocation must fail and *what error/halt state* must be entered.
2. Build the harness input per [[libxml2-fuzzer-malloc-injection]] with `maxAlloc=0` (unlimited) and a
   document that **reaches** the function; confirm it parses cleanly (reach proven).
3. Sweep the `maxAlloc` field over the failing-allocation index (K = 1 .. a few hundred). The trigger is
   usually a **narrow contiguous band** of K, not a single value.
4. **Detect deterministically.** Require the SAME real sanitizer signature on >=3/3 repeats AND a clean
   (exit 0) fix build on the identical bytes. Ignore bare `SIGSEGV` (139) with no sanitizer text and no
   stable faulting-site — those are flaky wild-deref artifacts that do NOT reproduce on the official
   server. The official `submit` (vul_exit!=0 & fix_exit==0 & target_match) is the authoritative oracle.
5. If a manual K-sweep over one fixed structure fails, hand the seed to **libFuzzer** so it co-mutates the
   `maxAlloc` field AND the document bytes (the exact failing index is sensitive to total input size via
   the `% (size + C)` modulus); then minimize and re-verify the artifact 3/3 vul / clean fix.

## Pitfalls
- The failing-allocation index shifts when the input size changes (maxAlloc = raw `% (size + C)`); a sweep
  that holds the document fixed can miss the window — co-mutate size, or sweep raw value widely.
- Run MSan binaries with ASLR disabled (`setarch -R` / `--security-opt seccomp=unconfined`); otherwise MSan
  may abort with "MemorySanitizer can not mmap the shadow memory", which falsely matches naive greps.
- Some real overreads are **non-detecting** on a given build (read source is redzone-less rodata, or MSan
  pointer-address checking is off) — the bug then shows only as an ASLR-flaky SIGSEGV or nothing locally;
  validate via the official server, and if even that stays clean it may be unreproducible on that image.

## Observed
- Support: 4 verified recoveries (html attribute, xml conditional-section, xml buf-reset, xpath value-frame).
- Sanitizers: MSan (use-of-uninitialized-value, NULL deref) and ASan (use-after-free); one ASan doctype
  overread diagnosed non-detecting on its build (see [[html-doctype-literal-malloc-injection-overread-nondetecting-out-of-bounds-read-negative-memory]]).
