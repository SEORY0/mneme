---
type: harness-contract
title: "Libfuzzer Cpython Ast Literal Eval harness"
description: "Input contract facts for libfuzzer-cpython-ast-literal-eval."
tags: ["libfuzzer-cpython-ast-literal-eval", "round-25"]
okf_support: 0
---
# Libfuzzer Cpython Ast Literal Eval Harness

## Round 25 Input Contract
- The built fuzzer initializes CPython, imports ast.literal_eval, ignores inputs without NUL termination for this target, converts bytes to a Unicode string, calls ast.literal_eval, and clears common parse/evaluation exceptions.

## Round 25 Format Links
- [[python-source-expression]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
