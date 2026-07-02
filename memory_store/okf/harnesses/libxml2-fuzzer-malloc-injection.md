---
type: harness-contract
title: "libxml2 fuzzer (malloc-injection) harness"
description: "Input contract for the libxml2 fuzz/ targets (html, xml, xpath) and their allocation-failure injector."
tags: ["libxml2-fuzzer-malloc-injection", "oom-injection", "maxalloc"]
okf_support: 4
provenance: claude-precise-analysis-2026-06-29
---
# libxml2 Fuzzer (malloc-injection) Harness

## Allocation-failure injector (shared)
`xmlFuzzMemSetLimit(maxAlloc)` makes `xmlFuzzMalloc/Realloc` return NULL on the **maxAlloc-th**
allocation (`fuzzNumAllocs >= maxAlloc - 1`); `maxAlloc = 0` means unlimited. Integers are read
**big-endian from the front** (`xmlFuzzReadInt`). Strings (`xmlFuzzReadString`) are terminated by a
backslash byte `0x5C` followed by newline `0x0A`; a literal backslash is doubled.

## Input layout per target binary
- **/out/html** (html.c): `opts[4 BE]` + `maxAllocRaw[4 BE]` (effective = raw `% (size+1)`) +
  `DOC` (remaining bytes). DOC is parsed by `htmlReadMemory` (pull) then re-fed in fixed chunks to the
  push parser.
- **/out/xml** (xml.c): `opts[4 BE]` + `maxAllocRaw[4 BE]` (effective = raw `% (size+100)`) +
  a sequence of (url-string)(content-string) pairs. The **first pair** is the main entity: content =
  the XML document, url = its base URL. **Later pairs** supply external resources (external DTD /
  external parameter-entity); the fuzz entity loader returns a pair whose url **equals the SYSTEM id**
  the document references. `opts` must enable the features the path needs: `XML_PARSE_DTDLOAD` to load an
  external subset, `XML_PARSE_NOENT` to expand entities (loads external parameter-entity content).
- **/out/xpath** (xpath.c): **NO opts field.** `maxAllocRaw[4 BE]` (effective = raw `% (size+1)`) +
  `EXPR-string` + `XML-string`. The XML doc is parsed with NO malloc limit; the limit is armed ONLY
  around the XPointer evaluation. An expression is only handed to the XPath evaluator if it is wrapped
  in an XPointer scheme — `xpointer(...)` or `xpath1(...)`; a bare expression is treated as a scheme
  name / child-sequence and never evaluated.

## Format Links
- [[html-document]]
- [[xml-with-external-subset]]
- [[xpointer-expression]]

## Notes
- Descriptive harness-carving facts only; not a causal claim. Pair with strategy
  [[malloc-failure-injection]].
- Reach the function with `maxAlloc=0` first, then sweep `maxAlloc` to fail the specific allocation on
  the bug's error/cleanup path. The trigger index shifts with total input size (the `% (size+C)`
  modulus), so co-mutating size (libFuzzer) is often faster than a fixed-structure sweep.
