# PHP fuzzer execute format contract

- format: `php-fuzzer-execute`
- related_policy: [[php-fiber-bailout-destructor]]

## Contract
The execute harness consumes a single raw PHP source buffer and compiles it as an in-memory request. The local libFuzzer wrapper may report directory-shaped corpus expectations, but the official submission artifact is still the source file itself.

## Gates
Keep the source below the execute fuzzer size limit. The useful path is runtime execution, not parser diagnostics: the code must compile, enter userland execution, start or resume a fiber, and then reach the fuzzer bailout cleanup state.

## Sink Invariant
The recovered crash shape keeps fiber-owned execution state alive until the fuzzer budget bailout and then reaches fiber cleanup or suspension while destructors are still capable of running.
