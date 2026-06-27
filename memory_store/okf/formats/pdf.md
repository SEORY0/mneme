---
type: format-family
title: pdf format
description: Structure, build skeleton, and bug-prone areas of the pdf input format.
resource: cybergym://format/pdf
tags: [pdf]
timestamp: 2026-06-24T00:00:00Z
okf_support: 4
---
# Schema
## Identification
Adobe PDF. Starts with `%PDF-1.x`; ends with `startxref`/`%%EOF`. mupdf/pdfium/poppler are lenient
and RECONSTRUCT a broken xref, so a minimal hand-built PDF usually parses.

## Structure
- Objects: `N 0 obj … endobj`. Body dicts `<< /Key val >>`, arrays `[ … ]`, streams `<<…>>stream\n…endstream`.
- Document: Catalog → Pages → Page(s); a Page has `/Contents` (a content-stream) + `/MediaBox` + `/Resources`.
- xref table + `trailer << /Root N 0 R /Size M >>` + `startxref <offset>`.
- **Content streams** are a postfix operator language: `q`/`Q` (save/restore gstate), `re` (rect path),
  `W`/`W*` (clip), `n`/`f`/`S` (paint), `BT…ET` (text), `BDC`/`BMC`/`EMC` (marked content).

## Where bugs hide (observed)
- Content-stream operators with unbounded nesting/state. (Real pattern: each `W` clip pushed a
  CLIP_MARK into a fixed `int nest_mark[256]` field WITHOUT the bounds check that guarded the
  marked-content push; >256 clip ops overran the heap-allocated processor struct → heap-overflow WRITE.)

## How to build (raw bytes; xref optional thanks to reconstruction)
```python
def pdf(content):
    objs=[b"<</Type/Catalog/Pages 2 0 R>>", b"<</Type/Pages/Kids[3 0 R]/Count 1>>",
          b"<</Type/Page/Parent 2 0 R/MediaBox[0 0 200 200]/Contents 4 0 R/Resources<<>>>>",
          b"<</Length %d>>stream\n"%len(content)+content+b"\nendstream"]
    out=b"%PDF-1.5\n"
    for i,o in enumerate(objs,1): out+=b"%d 0 obj"%i+o+b"endobj\n"
    return out+b"trailer<</Root 1 0 R/Size 5>>\n%%EOF"
poc = pdf(b"0 0 50 50 re W n "*400)   # >256 clip marks -> clip-stack overflow
```

## Reachability
The page must be renderable for the content stream to execute (`fz_run_page`). Keep Catalog→Pages→Page
intact and a non-empty `/Contents`.

# Examples
- Support: 4 train-set solves.
- Winning strategies (observed): {'fuzzer': 1, 'seed-sweep': 2, 'construct': 1}
- Format families (observed): {'pdf': 4}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, heap-buffer-overflow:WRITE, heap-use-after-free:READ, use-of-uninitialized-value:?

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
## Round 3 Verified Contracts
- [[pdf-xref-stream-negative-width]]: XRef stream dictionaries can drive signed sizing disagreement during entry parsing.
- [[pdf-invalid-indirect-resource]]: Renderable page resources can carry invalid indirect references into rasterization if the catalog, pages tree, and page dictionary stay coherent.

## Round 4 Verified Contracts
- [[pdf-inline-image-negative-dimension]]: Inline image dictionaries in a renderable page content stream can carry negative dimensions into stream skip/read arithmetic.

## Round 6 Factual Contract

### Schema / Invariants
- PDF inputs need a version marker, catalog, pages tree, page objects, trailer/root, and usually a coherent xref or enough structure for MuPDF repair. The relevant path is page lookup over the forward page map.
- PDF inputs can use plain xref tables, repaired missing xrefs, object streams, indirect page/resource objects, annotations, and form XObjects. MuPDF will attempt to repair malformed xref state, but target reachability depends on object-cache and xref-entry lifetimes rather than simple syntax acceptance.
- The relevant PDF path uses page annotations with string objects that can be literal or hex encoded. Poppler routes BOM-prefixed UTF-8 strings through UTF-8-to-UTF-16 conversion when objects are read by the Lexer and later consumed by annotation code.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 7 Factual Contract

### Schema / Invariants
- PDF reachability requires a catalog, pages tree, page object, resources with a font, and a content
stream. Poppler only asks SplashFTFont for a glyph path for stroked or clipped text rendering modes;
ordinary filled text does not use this path. A degenerate text matrix can drive a zero text scale in
the FreeType font wrapper.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 8 Factual Contract

### Schema / Invariants
- The harness consumes raw PDF bytes. A minimal catalog/pages/page/content structure is enough to reach rendering. PDF image data can be supplied either as inline images in a content stream or as external XObject images with masks/soft masks; negative image dimensions are rejected before the unpack path.
- A PDF can enter repair mode when its xref information is absent or invalid. Object streams are indirect stream objects whose dictionary declares object count, first-object area, and stream length; malformed metadata can be encountered during repair scanning.
- PDF reachability for Ghostscript requires a recognizable PDF header, catalog, pages tree, page object with media box, page resources including fonts, and a content stream. Ghostscript can recover from some non-canonical object ordering and stream/xref inconsistencies, but the page must still be renderable. Text operations are postfix content-stream operators inside BT/ET; TJ consumes an array whose elements are strings or numeric glyph displacements.
- The PDF needs a valid object graph with catalog, page tree, page resources, content stream, shading resource, and calculator function stream. Rendering the page, not merely parsing objects, is what executes the function program.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 9 Factual Contract

### Schema / Invariants
- PDF inputs for this harness are complete raw documents.
- Useful corpus samples have a normal PDF envelope with indirect objects, content streams, pages,
  fonts, and xref/trailer data; parser reach depends on a loadable document and at least one page
  renderable by Poppler.
- The PDF harness expects a complete PDF byte stream with header, indirect objects, xref/trailer,
  and a catalog.
- Rendering requires a page tree and at least one page object; content streams and image XObjects
  can have independent stream dictionaries, filters, declared lengths, and resource references.
- PDF inputs are complete raw documents.
- Parser reach requires recognizable PDF structure with xref/trailer and at least one page;
  malformed content streams or resource objects can still be repairable enough for MuPDF to render
  and enter image/bitmap handling.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 10 Factual Contract

### Schema / Invariants
- PDF input is accepted as raw file bytes. Poppler needs a normal header, catalog/pages/page graph, valid xref or recoverable objects, and stream dictionaries with Length entries before page rendering or stream construction paths are exercised.
- The PDF needs a header, catalog, pages node, page object, resources dictionary with a usable font, and a content stream whose declared length matches parseable text operators. A simple text object is sufficient to drive glyph metadata creation.
- The input must be a loadable PDF document with enough catalog, page, xref/trailer, and page resources for Poppler to create pages and render them. Broken-file reachability depends on preserving document repair gates while corrupting a narrow object/resource relation.
- Renderable PDFs need a valid page tree, resources, font references, and content streams. Font-related crashes are best approached from real PDFs that embed or select fonts which drive FreeType glyph loading rather than from a bare object skeleton.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-raw-pdf-renderer]]
- [[raw-pdf-text-extraction-render-harness]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 11 Factual Contract

### Schema / Invariants
- The input must be a complete renderable PDF, not a standalone stream object. A useful skeleton contains a catalog, pages tree, page, content stream, trailer, and startxref. Ghostscript can repair malformed cross-reference data, but ordinary repair of xref/startxref or stream lengths is not sufficient by itself.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 11 Factual Contract

### Schema / Invariants
- A renderable PDF needs a header, catalog, pages tree, page object, media box, resources dictionary, content stream, and image XObject stream. PDF image XObjects declare width, height, bits per component, colorspace, interpolate flag, stream length, and image data; page content invokes an image resource with graphics-state transforms.

### Harness Links
- [[libfuzzer-mupdf-pdf-renderer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
