import copy
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "tests"))
import test_executable_claims as executable  # noqa: E402
from claimlog import catalogue_markdown, load_claims, summary_markdown, validate_claim, validate_log  # noqa: E402

CLAIMS = load_claims(os.path.join(ROOT, "data", "claims.json"))


def by(verdict):
    return [c for c in CLAIMS if c["verdict"] == verdict]


def test_shipped_log_is_valid():
    assert validate_log(CLAIMS) == {} and len(CLAIMS) == 27


def test_verdict_mix_is_realistic():
    assert len(by("supported")) == 6 and len(by("contradicted")) == 19
    assert len(by("partially_supported")) == 1 and len(by("unverifiable")) == 1


def test_every_claim_has_a_primary_source_and_dated_check():
    for c in CLAIMS:
        assert any(s["source_type"] == "primary" for s in c["sources"])
        assert c["verification"]["date"] == "2026-10-22"


def test_every_executed_locally_claim_points_to_a_real_test():
    local = [c for c in CLAIMS if c["verification"]["method"] == "executed_locally"]
    assert len(local) == 10
    for c in local:
        fn = getattr(executable, c["verification"]["test"], None)
        assert callable(fn), c["verification"]["test"]
        fn()  # the referenced test must pass


def test_secondary_quote_claims_are_flagged_for_primary_check():
    flagged = [c for c in CLAIMS if c["verification"]["method"] == "online_secondary_quote"]
    assert {c["id"] for c in flagged} == {"VL-003", "VL-015", "VL-016"}
    for c in flagged:
        assert "primary" in c["rationale"].lower() or "open" in c["rationale"].lower()


def test_validator_catches_inconsistent_verdicts():
    c = copy.deepcopy(by("supported")[0])
    c["error_type"] = "factual_error"
    assert any("supported claim" in e for e in validate_claim(c))
    c = copy.deepcopy(by("contradicted")[0])
    c["severity"] = "none"
    assert any("needs an error_type" in e for e in validate_claim(c))
    c = copy.deepcopy(by("contradicted")[0])
    c["error_type"] = "unsupported_prediction"
    assert any("only valid for unverifiable" in e for e in validate_claim(c))


def test_validator_catches_source_and_evidence_problems():
    c = copy.deepcopy(CLAIMS[0])
    c["sources"] = [{**c["sources"][0], "source_type": "secondary"}]
    assert any("primary source" in e for e in validate_claim(c))
    c = copy.deepcopy(CLAIMS[0]); c["sources"][0]["url"] = "http://x.example"
    assert any("https" in e for e in validate_claim(c))
    c = copy.deepcopy(CLAIMS[0]); c["evidence"] = "word " * 80
    assert any("evidence is longer" in e for e in validate_claim(c))
    c = copy.deepcopy(CLAIMS[0]); c["rationale"] = "Too short."
    assert any("rationale" in e for e in validate_claim(c))
    c = copy.deepcopy(CLAIMS[0]); c["verification"] = {"method": "executed_locally", "date": "2026-10-22"}
    assert any("name the test" in e for e in validate_claim(c))
    c = copy.deepcopy(CLAIMS[0]); c["verification"]["date"] = "22/10/2026"
    assert any("YYYY-MM-DD" in e for e in validate_claim(c))


def test_duplicate_detection():
    problems = validate_log(CLAIMS + [copy.deepcopy(CLAIMS[0])])
    assert "duplicate id" in problems["VL-001"] and "duplicate claim text" in problems["VL-001"]


def test_reports_render():
    s = summary_markdown(CLAIMS)
    assert "27 AI-style claims" in s and "21 not fully supported" in s and "High-severity findings" in s
    log = catalogue_markdown(CLAIMS)
    assert log.count("## VL-") == 27 and "Rationale" in log
