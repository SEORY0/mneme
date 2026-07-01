---
type: format-family
title: PostScript DSC document
description: Abstract format contract for PostScript DSC document verifier-causal recoveries.
resource: cybergym://format/postscript-dsc
tags: [postscript-dsc, format_contract]
okf_support: 1
---
# PostScript DSC document

## Identification
DSC reachability requires a valid PostScript/comment envelope and recognized directive syntax.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep the directive delimiter recognized and place the invariant at the empty or malformed token consumed after that delimiter.

## Linked Policies
[[postscript-dsc-empty-token-uninitialized-text]]

## Round 35 Factual Contract

### Schema / Invariants
- The input is raw PostScript/DSC text. The scanner recognizes DSC comments beginning with percent-comment directives, parses optional header comments, defaults, setup, pages, and trailer sections, and accepts either structured PS-Adobe envelopes or unstructured PostScript text. Recognized directives often parse the token after a colon and then compare it against known keywords such as page order, orientation, media names, page counts, or atend markers.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
