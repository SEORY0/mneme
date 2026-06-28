---
type: format-family
title: PostScript program format
description: Format contract for PostScript programs that exercise interpreter stream and font paths.
resource: cybergym://format/postscript
tags: [postscript, text-expr, interpreter, stream]
timestamp: 2026-06-26T00:00:00Z
okf_support: 3
train_only: true
---
# Schema
## Structure
PostScript inputs are programs, not raw stream objects. A useful minimal carrier keeps syntax valid, creates a string or object that selects the vulnerable interpreter path, and then immediately invokes the operation that consumes that object.

## Invariants
- Syntax errors and undefined operators usually stop before the target runtime path.
- Filename and stream bugs need a decoded object that is accepted by the language layer but invalid for the lower stream layer.
- Keep the program compact so the first observable failure is attributable to the selected operation.

# Examples
- Support: 1 server-verified round solve.
- Winning strategy observed: construct a valid program whose filename decoding produced a broken stream object, then consume it immediately.

# Citations
- Distilled from a server-verified round solve with this format.

## Round 8 Factual Contract

### Schema / Invariants
- The parser accepts raw PostScript/EPS streams with DSC comments such as document header, page count, bounding boxes, page records, and showpage content. DSC fields may use deferred or per-page forms, but well-formed minimal documents are handled cleanly.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- PostScript arrays are normally delimited by a mark object from an opening bracket and consumed by the closing bracket. A closing bracket without a matching mark can interact with stack recovery and operators that expect preserved operands.
- The trigger requires a PostScript program that installs a subclassing or forwarding output device, obtains the underlying output child with .currentoutputdevice, causes an error or parameter transition that unsubclasses and frees the child, then sends later device operations through the stale device reference.

### Harness Links
- [[libfuzzer-ghostscript-postscript]]
- [[libfuzzer-gstoraster-stdin]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
