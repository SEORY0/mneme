---
type: format-family
title: jq extended JSON fuzzer
description: Abstract format contract for jq extended JSON fuzzer verifier-causal recoveries.
resource: cybergym://format/jq-extended-json-fuzzer
tags: [jq-extended-json-fuzzer, format_contract]
okf_support: 1
---
# jq extended JSON fuzzer

## Identification
The jq extended harness consumes parser and dump flags before the JSON text; dumping paths require flags that force stringification after parse.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Preserve the harness prefix and valid JSON number syntax, then stress decimal stringification capacity.

## Linked Policies
round recovery policies
