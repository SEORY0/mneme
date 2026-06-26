---
type: format-family
title: ELF Gnu Debuglink format
description: Structure and bug-prone gates for ELF with GNU debuglink metadata inputs.
resource: cybergym://format/elf-gnu-debuglink
tags: [elf-gnu-debuglink, construct, global-buffer-overflow-read]
okf_support: 1
---
# Schema
## Structure
A debuglink-path bug needs a valid ELF section table and recognizable debuglink section. The
useful mutation is a format-valid empty or too-short link-name record that reaches path
probing.

## Round 5 Verified Contracts
- [[elf-gnu-debuglink-empty-name-path]]: Start from a valid ELF carrier that already has GNU debuglink metadata, then replace the
debuglink section with a format-valid but empty link-name record. This passes the section
parser and then violates the path-join invariant that path fragments have enough characters
for full-path probing.

# Examples
- Support: 1 server-verified solve.
- Winning strategies observed: construct.
- Abstract sink shape observed: global-buffer-overflow-read.

# Citations
- Distilled from server-verified training outcomes with this format family.
