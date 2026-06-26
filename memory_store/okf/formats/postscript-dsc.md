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
