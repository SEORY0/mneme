---
type: format-family
title: PCRE2 fuzzer
description: Abstract format contract for PCRE2 fuzzer verifier-causal recoveries.
resource: cybergym://format/pcre2-fuzzer
tags: [pcre2-fuzzer, format_contract]
okf_support: 1
---
# PCRE2 fuzzer

## Identification
The PCRE2 fuzzer consumes option/control bytes before regex text.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Supply the required option prefix and keep the regex body minimal when the target is a JIT prescan or lookahead bounds issue.

## Linked Policies
round recovery policies
