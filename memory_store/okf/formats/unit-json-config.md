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

## Round 23 Factual Contract

### Schema / Invariants
- NGINX Unit configuration is a JSON object with top-level members such as listeners, routes, applications, and upstreams. Listener object keys and upstream server object keys are parsed as socket addresses. Addresses beginning with a colon have an empty host part before the port separator.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
