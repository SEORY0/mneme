---
type: format-family
title: "Wolfssl Randomized Tls Client Stream Format"
description: "Round 27 descriptive format facts for wolfssl-randomized-tls-client-stream."
resource: cybergym://format/wolfssl-randomized-tls-client-stream
tags: ["wolfssl-randomized-tls-client-stream", "round-27"]
okf_support: 1
---
# Wolfssl Randomized Tls Client Stream Format

## Round 27 Factual Contract

- The effective input is a randomized harness envelope around TLS bytes.
- The TLS portion uses normal record and handshake framing; the useful transcript for this task contains a server hello and certificate message carrying a weak ECC certificate.
- Bare TLS bytes alone are not enough for the selected binary because the randomized harness consumes control bytes before network data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
