---
type: format-family
title: MVG vector drawing format
description: Format contract for GraphicsMagick MVG text inputs that drive draw primitives.
resource: cybergym://format/mvg
tags: [mvg, text-expr, vector-drawing, geometry]
timestamp: 2026-06-26T00:00:00Z
okf_support: 3
train_only: true
---
# Schema
## Structure
MVG is a line-oriented vector drawing format. A runnable minimal input begins with a
`viewbox` line so the MVG reader allocates a canvas, followed by drawing primitives.

Useful skeleton:
- `viewbox x0 y0 x1 y1`
- one primitive line such as `ellipse cx,cy rx,ry start,end`

The parser accepts decimal numeric fields, including large integer-like values and
scientific notation. For geometry bugs, prefer a tiny canvas and mutate only the
geometry field that reaches the target primitive.

## Invariants
- `viewbox` must appear near the start, or the input is not recognized as MVG.
- Radius values must be non-negative to pass the draw primitive validation.
- For ellipse allocation bugs, keep the angular span ordinary and increase the radius
  until the point-count calculation crosses the vulnerable allocation boundary.
- Avoid unrelated corruption after the primitive; it destroys attribution and often exits
  before the geometry path.

# Examples
- Support: 1 server-verified train solve.
- Winning strategy observed: construct a minimal MVG envelope, then grow only the
  ellipse radius field until the vulnerable renderer crashes while the fixed build exits.

# Citations
- Distilled from a server-verified train solve with an MVG ellipse geometry bug.

## Text annotation expansion
- Text annotation expansion bugs require a valid canvas plus a text primitive that invokes image-attribute lookup.
- Keep geometry ordinary when the described sink is text translation; mutate only the attribute key shape.
- A parser-reached sink-match signal on text expansion is stronger evidence than a generic renderer crash elsewhere.

## Round 6 Factual Contract

### Schema / Invariants
- MVG is line-oriented text. The reader recognizes the format from a leading viewbox-style line, uses that viewbox to allocate the canvas, then renders subsequent primitive commands such as ellipse, polygon, path, and line. Geometry fields parse as decimal numbers; radius values must remain syntactically valid and non-negative.

### Harness Links
- [[libfuzzer-raw-mvg-blob]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 11 Factual Contract

### Schema / Invariants
- MVG is a line-oriented vector drawing format. A minimal document can begin with a viewbox/canvas declaration followed by drawing primitives. The ellipse primitive carries center coordinates, radii, and angle bounds as decimal fields; this parser path has no checksum or container header beyond recognizable MVG syntax.

### Harness Links
- [[libfuzzer-graphicsmagick-mvg]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- MVG is line-oriented drawing text with commands such as viewport setup, graphic-context control,
  paint attributes, and image compositing. URL-bearing arguments are tokenized by the shared Magick
  token scanner; quoting changes whether delimiters are treated as syntax or literal content.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- MVG is text and line oriented.
- A canvas/view declaration can be followed directly by drawing primitives; primitive geometry fields are parsed as numeric tokens without an outer binary container.

### Harness Links
- [[graphicsmagick-mvg-raw-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 19 Factual Contract

- MVG is accepted as raw drawing commands. A path primitive can contain SVG-like move, line, and curve commands inside quoted path data; polyline/polygon primitives are separate MVG records. Path rendering converts parsed primitive points into a PathInfo array and adds ghostline closure entries for open subpaths.
- Harness link: [[afl-libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 21 Factual Contract (libfuzzer-afl-wrapper)

### Schema / Invariants
- MVG input is text beginning with a viewbox declaration. Drawing state directives such as stroke, fill, stroke-dasharray, and stroke-dashoffset precede primitive geometry such as a line. The dash array parser accepts numeric lists, duplicates odd-length arrays internally, and appends a zero terminator.

### Harness Links
- [[libfuzzer-afl-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
