---
type: format-family
title: unit-json-config format
description: Structure and reachability facts for unit-json-config inputs.
tags: [unit-json-config]
okf_support: 0
---
# Unit Json Config Format

## Round 10 Factual Contract

### Schema / Invariants
- Unit configuration is JSON with top-level members such as access-log, routes, listeners, applications, and settings. Access-log objects require a nonempty path and can contain templated format and conditional fields. Backtick strings select the JavaScript-template branch, while dollar strings select the variable branch.

### Harness Links
- [[libfuzzer-json]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
