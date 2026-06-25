from mneme import ab_eval

SPLIT = {"train": ["t1", "t2"], "eval": ["e1"]}

def test_refuses_eval_tasks():
    rep = ab_eval.run(["e1"], SPLIT, memory_on=True, dry_run=True)
    assert rep.refused_eval == ["e1"]

def test_dry_run_report_has_required_metrics():
    rep = ab_eval.run(["t1", "t2"], SPLIT, memory_on=True, dry_run=True)
    for k in ("attempted", "target_matched", "median_attempts", "submit_count", "failure_classes"):
        assert k in rep.metrics
