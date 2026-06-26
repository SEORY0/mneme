---
type: format-family
title: Data URL
description: Abstract format contract for Data URL verifier-causal recoveries.
resource: cybergym://format/data-url
tags: [data-url, format_contract]
okf_support: 1
---
# Data URL

## Identification
A data URL parser first separates the MIME segment from payload and may synthesize defaults when the type is omitted.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Use a syntactically valid URL and place the lifetime edge in MIME parameter handling rather than malformed URL bytes.

## Linked Policies
[[data-url-temporary-mime-view-uaf]]
