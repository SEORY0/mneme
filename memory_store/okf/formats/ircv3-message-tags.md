---
type: format-family
title: "Ircv3 Message Tags Format"
description: "Round 27 descriptive format facts for ircv3-message-tags."
resource: cybergym://format/ircv3-message-tags
tags: ["ircv3-message-tags", "round-27"]
okf_support: 1
---
# Ircv3 Message Tags Format

## Round 27 Factual Contract

- IRCv3 message tags are accepted only at the start of an incoming line.
- The tag section begins with a marker, contains semicolon-separated key/value pairs, and ends at the command separator.
- Tag values support backslash escapes for separators and control characters, so a trailing escape is interpreted by the tag unescape routine rather than by the main command parser.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
