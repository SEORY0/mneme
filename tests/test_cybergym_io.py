from memonaemo import cybergym_io


def test_images_for(tmp_path):
    (tmp_path / "meta.json").write_text('{"id": "42537730"}')
    imgs = cybergym_io.images_for(tmp_path)
    assert imgs["vul_image"].endswith("42537730-vul")
    assert imgs["fix_image"].endswith("42537730-fix")


def test_parse_submit_redacts_in_repr(tmp_path):
    (tmp_path / "submit.sh").write_text(
        'curl -X POST http://srv:8080/submit-vul -d \'{"task_id":"arvo:1","agent_id":"a1","checksum":"c1"}\''
    )
    meta = cybergym_io.parse_submit(tmp_path)
    # The object can hold the values, but its repr/excerpt must redact them.
    assert "arvo:1" not in repr(meta)
