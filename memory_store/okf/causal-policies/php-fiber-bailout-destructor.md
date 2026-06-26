# PHP fiber bailout destructor recovery

- key: `no_crash x harness_input_shape_mismatch`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[php-fuzzer-execute]]

## Failure Shape
When a PHP fiber cleanup task verifies as a directory-shape mismatch or clean execution, the usual dead end is treating the harness as a command-line PHP runner. The execute fuzzer consumes one raw PHP source buffer. Inputs that only start and resume a fiber without forcing a fuzzer-step bailout tend to finish normally or miss the unsafe cleanup state.

## Procedure
Use the raw PHP source file as the submitted artifact. Build a compact script that starts a fiber, keeps destructible state reachable inside that fiber, and forces execution past the fuzzer step budget while the fiber can still be destroyed or suspended during cleanup. Keep the script small enough for the execute fuzzer size gate and avoid any corpus-directory wrapper in the official submission path.

## Verifier Contract
The expected local signal is a sanitizer crash in fiber suspension or fiber cleanup after the fuzzer execution loop bails out. The official gate should distinguish vulnerable and fixed builds; a file that only triggers parser or command-line errors is not a solve.

## Negative Guards
Do not submit a directory to the official endpoint. Do not rely on ordinary fatal errors or uncaught PHP exceptions alone; they can bypass the unsafe destructor path or be handled consistently by both builds.
