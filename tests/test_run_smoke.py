import subprocess, sys, json, os
from pathlib import Path


def test_solve_fake_smoke(tmp_path):
    # A fake backend + fake verifier path so no Docker/model/network is touched.
    task = tmp_path / "task"; task.mkdir()
    (task / "description.txt").write_text("heap overflow in parse, tiff input")
    (task / "meta.json").write_text('{"id": "0000-fake"}')
    run_dir = tmp_path / "run"
    env = {**os.environ, "PYTHONPATH": "src", "MEMONAEMO_FAKE": "1"}
    r = subprocess.run(
        [sys.executable, "runner/run.py", "solve", "--task-dir", str(task),
         "--run-dir", str(run_dir), "--fake"],
        capture_output=True, text=True, env=env,
    )
    assert r.returncode == 0, r.stderr
    result = json.loads((run_dir / "result.json").read_text())
    assert "failure_class" in result or "target_match" in result
    # D9 sanity: the agent transcript dir must not contain memory_store paths.
    assert not list(run_dir.rglob("memory_store"))


def test_d9_violation_fails_hard(tmp_path):
    """Regression test: D9 violation (memory_store under run_dir) must fail hard."""
    task = tmp_path / "task"; task.mkdir()
    (task / "description.txt").write_text("heap overflow, tiff input")
    (task / "meta.json").write_text('{"id": "0000-fake"}')
    run_dir = tmp_path / "run"; run_dir.mkdir(parents=True)
    # Plant D9 violation before invoking solve
    (run_dir / "memory_store").mkdir()
    env = {**os.environ, "PYTHONPATH": "src", "MEMONAEMO_FAKE": "1"}
    r = subprocess.run(
        [sys.executable, "runner/run.py", "solve", "--task-dir", str(task),
         "--run-dir", str(run_dir), "--fake"],
        capture_output=True, text=True, env=env,
    )
    assert r.returncode != 0, "D9 violation must fail hard (non-zero exit)"
    assert "memory_store" in (r.stderr + r.stdout).lower()
