---
type: format-family
title: pdf format
description: Structure, build skeleton, and bug-prone areas of the pdf input format.
resource: cybergym://format/pdf
tags: [pdf, "round-16"]
timestamp: 2026-06-24T00:00:00Z
okf_support: 21
---
# Schema
## Identification
Adobe PDF. Starts with `%PDF-1.x`; ends with `startxref`/`%%EOF`. mupdf/pdfium/poppler are lenient
and RECONSTRUCT a broken xref, so a minimal hand-built PDF usually parses.

## Structure
- Objects: `N 0 obj  endobj`. Body dicts `<< /Key val >>`, arrays `[  ]`, streams `<<>>stream\nendstream`.
- Document: Catalog  Pages  Page(s); a Page has `/Contents` (a content-stream) + `/MediaBox` + `/Resources`.
- xref table + `trailer << /Root N 0 R /Size M >>` + `startxref <offset>`.
- **Content streams** are a postfix operator language: `q`/`Q` (save/restore gstate), `re` (rect path),
  `W`/`W*` (clip), `n`/`f`/`S` (paint), `BTET` (text), `BDC`/`BMC`/`EMC` (marked content).

## Where bugs hide (observed)
- Content-stream operators with unbounded nesting/state. (Real pattern: each `W` clip pushed a
  CLIP_MARK into a fixed `int nest_mark[256]` field WITHOUT the bounds check that guarded the
  marked-content push; >256 clip ops overran the heap-allocated processor struct  heap-overflow WRITE.)

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
The page must be renderable for the content stream to execute (`fz_run_page`). Keep CatalogPagesPage
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

## Round 12 Factual Contract

### Schema / Invariants
- The target format is a complete PDF or PostScript job for Ghostscript's CUPS raster path. PDF xref streams are indirect stream objects with a trailer dictionary, width array, length, root reference, and startxref pointer. Declaring an empty xref table alone is not sufficient without a coherent document graph.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- PDF shading dictionaries can reference a Type 3 stitching function through the page resource shading table. A stitching function uses a single input domain, an array of subfunctions, boundary values, encode pairs, and an optional range array that determines the outer result arity. Subfunctions may independently declare their own range-derived arity.
- PDF object streams are stream objects declaring object count, first-object table size, and stream length; their data begins with object-number and relative-offset pairs followed by serialized objects. Reachability also needs a PDF header, trailer/root, catalog, pages tree, and renderable page graph.
- PDF inputs need a header, indirect catalog/pages/page objects, content stream, xref/trailer, and optional annotations or structure-tree objects to exercise annotation processors. MuPDF tolerates repairable structure but rendering must reach the page or annotation processor.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-ghostscript-device-wrapper]]
- [[libfuzzer-mupdf-pdf-renderer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 16 Factual Contract

### Schema / Invariants
- A minimal PDF needs a catalog, page tree, page, media box, and content stream to reach MuPDF page rendering. Content streams can drive clipping through path operators, image XObjects and image masks, Type3 glyph programs, and annotation appearance form XObjects. Broken xref data may be repaired, but rendering-specific bugs need a valid page graph.
- A minimal PDF needs a catalog, pages tree, page object, content stream, resources, and an image XObject. Page boxes and content-stream graphics state commands can make image painting degenerate by combining page geometry, transforms, and image draw operations.
- PDF repair depends on a recognizable PDF header plus enough object syntax for the repair scanner to rebuild object locations. Page trees, content streams, resources, annotations, object streams, xref tables, and xref streams can all force object dereferences during rendering, but malformed xref data alone is usually repaired or ignored cleanly.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-gstoraster]]
- [[libfuzzer-mupdf-pdf-renderer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- PDF objects can be kept minimal for this harness: catalog, pages, page, content stream, resources, and xref are enough to reach rendering.
- Shading resources invoke PDF functions during page rendering; Separation and DeviceN color spaces invoke tint functions during fill operations.
- Function dictionaries derive input count from Domain pairs and output count from Range or caller expectations.
- A minimal PDF page requires catalog, pages, page, contents, resources, and xref/trailer structure.
- MuPDF tolerates some malformed object graphs through repair, but repaired xref and missing-resource failures can remain off-target.
- Image resources need to be wired through page resources before rendering attempts to decode their streams.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- A PDF input needs the PDF header, catalog, pages tree, page object, resources, content stream, xref, and trailer. An Indexed color space is represented as an array with a base color space, maximum index, and lookup table. Pattern is a color-space category rather than a valid Indexed base and must be rejected when the color space is resolved for painting.
- A PDF begins with a version header, then objects, page tree data, optional streams, cross-reference information, trailer, and an end marker for deeper document loading. MuPDF will still attempt repair on damaged PDFs after seeing a plausible header, so very short headers can reach early version parsing even when the rest of the document is absent.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-ghostscript]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The PDF needs a catalog, pages tree, page resources, a content stream applying an ExtGState, a form XObject for the mask group, and a function object referenced as the soft-mask transfer function. Painting after selecting the ExtGState is what forces Ghostscript to begin the transparency mask.

### Harness Links
- [[libfuzzer-ghostscript-gstoraster]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The relevant PDF structure is a catalog, page tree, page, and annotation object. FreeText annotations need page linkage, a rectangle, default appearance string, and contents; odd or malformed Unicode contents can cause layoutText to return before initializing output values.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer-raw-poppler-renderer)

### Schema / Invariants
- A raw PDF needs a catalog, page tree, page object, annotation array, xref table, and trailer. Widget annotations under a page can also act as form fields when they carry form-field keys. A widget is treated as standalone when it is reachable from page annotations but absent from the AcroForm fields array.

### Harness Links
- [[libfuzzer-raw-poppler-renderer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- The attempted PDF carrier used a normal catalog, pages tree, page object, annotation array, widget annotations, and appearance Form XObjects. Annotation appearance streams are PDF content streams that can contain graphics-state save operations and drawing operators; invalid resources or operators can create rendering errors if the appearance is actually rendered.
- A small PDF with a catalog, pages tree, one page, resources, and a content stream is sufficient. The MuPDF parser is tolerant of simple repaired structure, so a fully polished cross-reference table is not necessary when the core page graph and stream objects are recognizable.
- A useful Poppler PDF for this path needs a catalog, pages tree, page resources, content stream, and an image-mask XObject. Image-mask rendering uses the current transformation matrix to choose scaling and can route to Splash mask scaling when the mask is enlarged relative to source dimensions.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- PDF inputs need a loadable catalog, pages tree, and page content or other renderable object before the fuzzer exercises stream construction during page rendering. Stream objects use dictionary-declared lengths followed by stream data and terminators; xref consistency helps keep seed mutations loadable.
- A minimal PDF only needs catalog, pages, one page, a content stream, and resource dictionaries. Function-based shadings load a shading dictionary with a color space and a Function object, then sample the function into an internal table before page rendering. Type-2 exponential functions accept Domain, Range, C0, C1, and N arrays/scalars.
- A compact PDF can trigger page rendering with only catalog, pages, one page, a content stream, and a page resources dictionary. PDF path operators can define a rectangle, mark it as the current clipping path, and end the path; repeating that sequence accumulates clip nesting during page interpretation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- PDF repair scans indirect objects and object streams when the xref table is missing or unusable. Object streams contain a declared count and a table of compressed object numbers paired with offsets before the embedded object bodies. Repair uses those object numbers to populate xref entries.
- A minimal PDF needs a version header, catalog, pages tree, page object, media box, and content stream. MuPDF can repair a simple missing or weak xref if the object graph is otherwise recognizable and renderable.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-ghostscript-gstoraster]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- Classic PDF xref tables consist of a header, subsections, fixed-width numeric entry fields with an in-use/free marker, a trailer dictionary, and a startxref pointer back to the xref section. Early xref processing can be reached with a very small document when those structural gates are coherent.

### Harness Links
- [[libfuzzer-qpdf]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- PDF reachability required a complete object graph rather than a header stub: catalog, pages node, page object, content stream, xref table, trailer, and startxref. PDFium accepted sub-unit page-box dimensions; at the default scale libvips rounded those dimensions to zero before downstream thumbnail processing.
- A minimal PDF that renders through this harness needs a catalog, pages tree, page dictionary with media box/resources, a contents stream with a self-consistent length, and a valid xref/trailer. Page content graphics operators can create a rectangle path, apply it as the clipping path, and clear the path; repeated clipping intersects the current clipping region and pushes nested draw-device state.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-raw-memory]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- The PDF parser accepts a normal document tree with catalog, pages, page, media box, optional crop box, resources, annotations, patterns, shadings, forms, and content streams. Empty MediaBox values are replaced by a default page rectangle, empty CropBox values are ignored, and non-overlapping CropBox intersections are sorted back into a non-empty page bound. Very small page bounds are normalized before page transform. The page unit value must be parsed as a real object; plain decimal real values were accepted more reliably than exponent-like spellings in page dictionaries.
- A PDF render path needs a catalog, pages tree, page object, media box, content stream, and resources dictionary. Shading resources are referenced from page content with the shading operator. A type 4 mesh shading stream is controlled by flag, coordinate, and component bit-width entries plus a decode array; mesh samples are packed bit fields read most-significant-bit first.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- A MuPDF-renderable PDF needs a recognizable header, catalog, pages tree, page dictionary, media box, page resource dictionary, content stream, xref table or repairable object layout, and trailer root. Page resources are named dictionaries for fonts, XObjects, shadings, patterns, ExtGState, and color spaces; content operators must reference those names to force resolution during rasterization. ToUnicode CMaps must be attached through a font resource, image and form XObject streams need stream dictionaries with dimensions or form bounds, and malformed xrefs may be repaired without reaching a sanitizer-visible sink.
- A PDF object stream is a stream object whose dictionary names an object count and the byte position where object bodies begin; the stream header lists object numbers and relative offsets. Cross-reference streams use compressed-object entries to point an object number at an object stream and index. Incremental updates can preserve a previous xref section through a previous-xref pointer, override an object, and introduce a newer generation for the same object number.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-pdf-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 32 Factual Contract

### Schema / Invariants
- PDF reachability for this harness requires a complete raw document with header, catalog, pages tree, page object, resources when rendering text, stream dictionaries, xref or xref-stream metadata, trailer/root linkage, startxref, and EOF marker. Ordinary content streams use a /Length field followed by stream data and endstream; object streams declare an object count, a First value for the object table area, and embedded object bodies. Xref streams declare Type XRef, Size, W field widths, optional compressed-object entries, and trailer keys in the stream dictionary.
- PDF reachability for this harness requires a complete raw document: version header, indirect catalog/pages/page objects, a page content stream, xref/trailer metadata, and EOF marker. Poppler can repair malformed xref material, but small changes to the xref table or stream dictionary can move from target reachability to clean rejection; stream dictionaries use declared lengths and endstream markers, while repaired xref state can override or validate stream boundaries.
- PDF reachability for this harness requires a recognizable header, indirect catalog/pages/page objects, a content stream, xref or repairable object locations, trailer/root linkage, and an EOF marker. Stream dictionaries can use indirect Length objects, and Poppler may repair or reconstruct xref state when an indirect reference is missing from the active table but present in the body.
- PDF linearization is parsed from the first indirect object. The declared document length must match the raw file length for Poppler to treat the file as optimized. In the linearized path, Poppler expects an xref table directly after the first object rather than only at EOF. The /H array identifies a byte range that is copied and parsed as an indirect hint stream; that stream dictionary uses /S to split page-offset hints from shared-object hints. A normal catalog, pages tree, page dictionary, content stream, trailer, and xref metadata are still useful so the harness reaches page rendering and the fixed build can fall back safely.
- A minimal renderable PDF needs a catalog, pages tree, page object, content stream, resource dictionary, and valid cross-reference table. Shadings in page content can force function evaluation during rendering. Axial shadings sample a function with one parameter; stitching functions can forward that single parameter to a subfunction; calculator and sampled functions derive their expected input count from Domain pairs and output count from Range pairs.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-raw-poppler-renderer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 33 Factual Contract

### Schema / Invariants
- A PDF image XObject can be reached from page resources and painted with a short content stream. A color-key /Mask array creates an alpha-bearing destination pixmap even when the source colorspace has only color components. MuPDF accepts image component depths beyond the common PDF fast paths as long as they are within its supported range; the image stream length must match the derived stride and height so the image is not merely truncated.
- PDF rendering needs a valid catalog, page tree, page, content stream, and resource dictionary. A shading resource can trigger Type 3 stitching functions during page painting. Function output arity is derived from Range entries, and subfunctions may have independent arity unless the parser enforces consistency.
- PDF AcroForm widget annotations can be drawn during page rendering when no appearance stream is supplied. Choice fields read options from the Opt array; invalid option entries may yield null display text. Default appearance and default resources must name a usable font before the appearance builder reaches text layout. Quadding controls whether measured text width affects emitted drawing commands.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-mupdf-pdf-render]]
- [[libfuzzer-poppler-pdf-render]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- A PDF can reach this path when it has a valid header, an initial linearization dictionary whose declared document length matches the actual input length, an xref/trailer with a Root and Encrypt entry, and enough catalog/page/content structure for rendering. The linearization H entry points to a byte range that is copied and parsed as a hint stream object.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
