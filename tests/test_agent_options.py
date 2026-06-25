from pathlib import Path
from memonaemo import agent_driver

def test_options_exclude_memory_store(tmp_path):
    run = tmp_path / "run"; run.mkdir()
    skills = tmp_path / "skills"; skills.mkdir()
    opts = agent_driver.build_options(run, skills, mcp_servers={}, model="claude-opus-4-8")
    # Whatever the SDK field is, the resolved allowed roots must not include memory_store.
    roots = agent_driver.allowed_fs_roots(opts)
    assert all("memory_store" not in str(r) for r in roots)
    assert any(str(run) in str(r) for r in roots)

def test_system_prompt_loaded(tmp_path):
    opts = agent_driver.build_options(tmp_path, tmp_path, mcp_servers={})
    assert "verify.run" in agent_driver.system_prompt_text(opts)
