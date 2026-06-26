---
type: format-family
title: mruby script format
description: Format contract for mruby scripts that exercise interpreter runtime conversion paths.
resource: cybergym://format/mruby-script
tags: [mruby, ruby, script, interpreter]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs are syntactically valid mruby scripts. Runtime bugs require the script to reach interpreter dispatch and construct receivers of the expected internal type before the vulnerable operation is called.

## Invariants
- Syntax errors and ordinary exceptions are not progress for sanitizer targets.
- Numeric conversion bugs can depend on receiver representation, such as bigint versus small integer.
- Put the invalid argument after selecting the receiver-specific path.

# Examples
- Support: 1 server-verified round solve.
- Winning strategy observed: create a bigint receiver, then pass an invalid base through the bigint conversion path.

# Citations
- Distilled from a server-verified round solve with this format.
