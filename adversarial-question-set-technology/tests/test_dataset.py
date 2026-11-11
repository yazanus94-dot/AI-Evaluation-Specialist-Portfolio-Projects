import copy
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from advqs import grade_answer, load_questions, validate_dataset, validate_question  # noqa: E402
from advqs.catalog import catalog_markdown, stats_markdown  # noqa: E402

QUESTIONS = load_questions(os.path.join(ROOT, "data", "questions.json"))


def test_shipped_dataset_is_valid():
    assert validate_dataset(QUESTIONS) == {}
    assert len(QUESTIONS) == 29


def test_dataset_is_balanced_enough():
    topics = {q["topic"] for q in QUESTIONS}
    traps = {q["trap_type"] for q in QUESTIONS}
    assert len(topics) >= 8 and len(traps) == 8
    assert sum(q["difficulty"] >= 3 for q in QUESTIONS) > len(QUESTIONS) / 2


def test_every_question_names_a_source_and_a_failure_mode():
    for q in QUESTIONS:
        assert q["source"]["title"] and q["source"]["reference"]
        assert q["expected_model_failure"] and q["why_hard"]


def test_verification_dates_are_present_when_verified():
    for q in QUESTIONS:
        v = q["verification"]
        assert (v["status"] == "needs_manual_check") == (v["date"] is None)


def test_validator_rejects_missing_and_bad_fields():
    q = copy.deepcopy(QUESTIONS[0])
    assert validate_question(q) == []
    bad = copy.deepcopy(q); del bad["reference_answer"]
    assert "missing field: reference_answer" in validate_question(bad)
    bad = copy.deepcopy(q); bad["difficulty"] = 9
    assert "difficulty must be an integer 1-5" in validate_question(bad)
    bad = copy.deepcopy(q); bad["trap_type"] = "trick"
    assert any("unknown trap_type" in e for e in validate_question(bad))
    bad = copy.deepcopy(q); bad["source"]["url"] = "http://insecure.example"
    assert any("https" in e for e in validate_question(bad))
    bad = copy.deepcopy(q); bad["key_points"] = ["only one"]
    assert any("key_points" in e for e in validate_question(bad))


def test_false_premise_and_outdated_rules():
    fp = copy.deepcopy([q for q in QUESTIONS if q["trap_type"] == "false_premise"][0])
    fp["reference_answer"] = "Here is a long answer that never says anything about the claim being wrong at all today."
    assert any("premise" in e for e in validate_question(fp))
    od = copy.deepcopy([q for q in QUESTIONS if q["trap_type"] == "outdated_fact"][0])
    od["reference_answer"] = "This answer has no date in it but is otherwise long enough to pass the length check."
    assert any("date the facts" in e for e in validate_question(od))


def test_duplicate_ids_and_questions_are_detected():
    dup = QUESTIONS + [copy.deepcopy(QUESTIONS[0])]
    problems = validate_dataset(dup)
    assert "duplicate id" in problems["AQ-001"] and "dataset" in problems


def test_grader_scoring_and_caps():
    q = [x for x in QUESTIONS if x["id"] == "AQ-001"][0]
    assert grade_answer(q, [True, True, True, True])["score"] == 100
    assert grade_answer(q, [True, True, False, False])["verdict"] == "partial"
    assert grade_answer(q, [True, False, False, False])["verdict"] == "fail"
    capped = grade_answer(q, [True, True, True, True], contains_fabrication=True)
    assert capped["score"] == 30 and capped["notes"]
    fp = [x for x in QUESTIONS if x["trap_type"] == "false_premise"][0]
    assert grade_answer(fp, [True] * len(fp["key_points"]), accepted_false_premise=True)["score"] == 0
    try:
        grade_answer(q, [True])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for wrong number of marks")


def test_catalogue_and_summary_render():
    cat = catalog_markdown(QUESTIONS)
    assert cat.count("## AQ-") == 29 and "Reference answer" in cat
    s = stats_markdown(QUESTIONS)
    assert "29 questions" in s and "Source verification status" in s
