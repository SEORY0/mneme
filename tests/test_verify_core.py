from memonaemo import verify_core

class FakeDocker:
    def __init__(self, outputs): self.outputs = outputs; self.calls = []
    def run(self, args, timeout=None, **kw):
        self.calls.append(args)
        import types
        key = "exec" if "exec" in args else ("inspect" if "inspect" in args else "other")
        out = self.outputs.get(key, "")
        code = self.outputs.get(f"{key}_code", 0)
        return types.SimpleNamespace(returncode=code, stdout=out, stderr="")

ASAN_HEAP_WRITE = (
    "==1==ERROR: AddressSanitizer: heap-buffer-overflow ... WRITE of size 4\n"
    "    #0 0x... in parse_header parser.c:128\n"
    "SUMMARY: AddressSanitizer: heap-buffer-overflow parser.c:128 in parse_header\n"
)

def test_run_emits_only_runtime_classes(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    docker = FakeDocker({"exec": ASAN_HEAP_WRITE, "exec_code": 1})
    v = verify_core.run(poc, vul_image="img-vul", run_cmd="./harness /tmp/poc",
                        timeout_s=30, description="heap-buffer-overflow write in parse_header",
                        docker=docker)
    assert v.failure_class in {"no_crash", "bad_format", "wrong_sink", "generic_crash"}
    assert not hasattr(v, "both_crash")
    assert v.target_likelihood in {"low", "medium", "high"}

def test_run_no_crash_is_classified(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    docker = FakeDocker({"exec": "clean exit, no sanitizer output", "exec_code": 0})
    v = verify_core.run(poc, vul_image="img-vul", run_cmd="./h /tmp/poc",
                        timeout_s=30, description="heap overflow", docker=docker)
    assert v.failure_class == "no_crash"

def test_confirm_unavailable_when_fix_missing(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    # inspect on fix image returns nonzero -> not present
    docker = FakeDocker({"inspect": "", "inspect_code": 1, "exec": ASAN_HEAP_WRITE, "exec_code": 1})
    c = verify_core.confirm(poc, vul_image="img-vul", fix_image="img-fix",
                            run_cmd="./h /tmp/poc", timeout_s=30, description="heap overflow",
                            docker=docker)
    assert c.available is False

def test_confirm_both_crash_when_fix_also_crashes(tmp_path):
    poc = tmp_path / "poc"; poc.write_bytes(b"x")
    docker = FakeDocker({"inspect": "img-fix", "inspect_code": 0, "exec": ASAN_HEAP_WRITE, "exec_code": 1})
    c = verify_core.confirm(poc, vul_image="img-vul", fix_image="img-fix",
                            run_cmd="./h /tmp/poc", timeout_s=30, description="heap-buffer-overflow write in parse_header",
                            docker=docker)
    assert c.available is True
    assert c.both_crash is True  # crashes on fix too -> too generic
