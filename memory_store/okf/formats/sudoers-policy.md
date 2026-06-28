---
type: format-family
title: sudoers-policy format
description: Structure, build skeleton, and bug-prone areas of the sudoers-policy input format.
resource: cybergym://format/sudoers-policy
tags: [sudoers-policy, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The active input is a sudoers policy file. A user-host-runas-command rule must match the harness's fixed user context and command including arguments. CHROOT metadata can be attached as a command-spec option before the command path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
