---
type: format-family
title: "Websocket Permessage Deflate Over Mocked Tcp Format"
description: "Round 26 descriptive structure and invariant facts for websocket-permessage-deflate-over-mocked-tcp."
tags: ["websocket-permessage-deflate-over-mocked-tcp", "round-26"]
okf_support: 1
train_only: true
---
# Websocket Permessage Deflate Over Mocked Tcp Format

## Round 26 Factual Contract

### Schema / Invariants
- The active input is not a standalone deflate buffer. It is a sequence of mocked socket chunks, each with a small length prefix followed by network bytes. WebSocket reachability requires a valid upgrade request and client frames must be masked. RSV1 marks a frame as permessage-deflate-compressed after the extension has been negotiated.

### Harness Links
- [[libfuzzer-uwebsockets-mocked-tcp]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
