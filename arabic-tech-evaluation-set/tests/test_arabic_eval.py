import copy
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from arabic_eval import (compute_score, expected_rating, lint_text, load_evaluations, load_glossary, load_rubric,  # noqa: E402
                         validate_dataset, validate_evaluation)
from arabic_eval.report import catalogue_markdown, lint_agreement, summary_markdown  # noqa: E402

D = os.path.join(ROOT, "data")
RUBRIC = load_rubric(os.path.join(D, "rubric.json"))
GLOSSARY = load_glossary(os.path.join(D, "glossary.csv"))
ITEMS = load_evaluations(os.path.join(D, "evaluations.json"))
ALL5 = {c["id"]: 5 for c in RUBRIC["criteria"]}


def with_scores(**kw):
    s = dict(ALL5); s.update(kw)
    return s


def types(text):
    return {f["type"] for f in lint_text(text, GLOSSARY)}


def test_rubric_weights_sum_to_one():
    assert abs(sum(c["weight"] for c in RUBRIC["criteria"]) - 1.0) < 1e-9


def test_score_extremes_and_weights():
    assert compute_score(ALL5, RUBRIC)[0] == 100.0
    assert compute_score({k: 1 for k in ALL5}, RUBRIC)[0] == 0.0
    only_terms_low = compute_score(with_scores(terminology=1), RUBRIC)[0]
    assert only_terms_low == 80.0  # terminology weighs 20%


def test_gates_cap_the_score():
    assert compute_score(with_scores(technical_accuracy=1), RUBRIC)[0] == 40.0
    assert compute_score(with_scores(instruction_following=2), RUBRIC)[0] == 60.0
    assert compute_score(with_scores(language_quality=2), RUBRIC)[0] == 60.0
    score, gates = compute_score(ALL5, RUBRIC, ["fabricated_source"])
    assert score == 20.0 and gates


def test_score_validates_input():
    for bad in ({k: v for k, v in ALL5.items() if k != "formatting"}, with_scores(formatting=6), with_scores(formatting=0)):
        try:
            compute_score(bad, RUBRIC)
        except ValueError:
            continue
        raise AssertionError("expected ValueError")


def test_expected_rating_bands():
    assert [expected_rating(x) for x in (0, 20, 20.1, 40, 60, 80, 80.1, 100)] == [1, 1, 2, 2, 3, 4, 5, 5]


def test_lint_flags_transliterated_terms_with_prefixes_and_articles():
    assert "discouraged_term" in types("امسح الكاش الخاص بالبراوزر")
    assert "discouraged_term" in types("شغّل الفاير وول")
    assert "discouraged_term" in types("أنشئ باك اب")
    found = lint_text("غيّر الباسوورد", GLOSSARY)
    assert found and found[0]["suggestion"].startswith("كلمة المرور")


def test_lint_normalizes_hamza_variants_and_diacritics():
    assert "discouraged_term" in types("ابليكيشن")
    assert "discouraged_term" in types("أبليكيشن")
    assert "discouraged_term" in types("البراوزر")


def test_lint_accepts_standard_terms_and_latin_abbreviations():
    assert lint_text("ذاكرة الوصول العشوائي (RAM) أسرع من القرص الصلب", GLOSSARY) == []
    assert lint_text("استخدم كلمة مرور قوية وحدّث المتصفح", GLOSSARY) == []


def test_lint_does_not_match_inside_longer_words():
    assert lint_text("المتصفح الحديث", GLOSSARY) == []


def test_lint_latin_punctuation_only_in_arabic_lines():
    assert "latin_punctuation" in types("ما هي لغة Python?")
    assert "latin_punctuation" in types("المعالج, والذاكرة")
    assert lint_text("What is Python? It is a language, quite popular.", GLOSSARY) == []
    assert lint_text("ما هي لغة Python؟", GLOSSARY) == []


def test_lint_mixed_numerals():
    assert "mixed_numerals" in types("عدد 5 و٦")
    assert "mixed_numerals" not in types("عدد 5 و6")


def test_glossary_integrity():
    english = [g["english"] for g in GLOSSARY]
    assert len(english) == len(set(english)) and len(GLOSSARY) == 19
    for g in GLOSSARY:
        assert g["preferred_ar"]
        assert g["preferred_ar"] not in g["discouraged"]


def test_shipped_dataset_is_valid_and_balanced():
    assert validate_dataset(ITEMS, RUBRIC) == {}
    assert len(ITEMS) == 30
    assert sum(e["rating"] == 5 for e in ITEMS) == 12
    assert all(e["review_status"] == "needs_native_review" for e in ITEMS)


def test_top_rated_arabic_responses_are_lint_clean():
    for e in ITEMS:
        if e["rating"] == 5 and e["response_lang"] == "ar":
            assert lint_text(e["response"], GLOSSARY) == [], e["id"]


def test_corrections_are_lint_clean():
    for e in ITEMS:
        if e.get("correction") and e["correction_lang"] == "ar":
            assert lint_text(e["correction"], GLOSSARY) == [], e["id"]


def test_lint_agrees_with_reviewer_tags():
    la = lint_agreement(ITEMS, GLOSSARY)
    assert la == {"hits": 5, "misses": 0, "false_alarms": 0}


def test_validator_catches_inconsistencies():
    e = copy.deepcopy(ITEMS[2])
    assert validate_evaluation(e, RUBRIC) == []
    bad = copy.deepcopy(e); bad["rating"] = 5
    assert any("inconsistent" in x for x in validate_evaluation(bad, RUBRIC))
    bad = copy.deepcopy(e); bad["correction"] = None
    assert any("corrected version" in x for x in validate_evaluation(bad, RUBRIC))
    bad = copy.deepcopy(e); bad["error_tags"] = []
    assert any("no error tag" in x for x in validate_evaluation(bad, RUBRIC))
    bad = copy.deepcopy(e); bad["error_tags"] = ["made_up"]
    assert any("unknown error tags" in x for x in validate_evaluation(bad, RUBRIC))
    fab = copy.deepcopy([x for x in ITEMS if "fabricated_source" in x["error_tags"]][0])
    fab["rating"] = 2
    assert any("must be rated 1" in x for x in validate_evaluation(fab, RUBRIC))
    clean = copy.deepcopy(ITEMS[0]); clean["error_tags"] = ["factual_error"]
    assert any("every score is 5" in x for x in validate_evaluation(clean, RUBRIC))


def test_reports_render():
    s = summary_markdown(ITEMS, RUBRIC, GLOSSARY)
    assert "30 responses evaluated" in s and "Automatic lint versus reviewer tags" in s
    cat = catalogue_markdown(ITEMS)
    assert cat.count("## AR-") == 30 and 'dir="rtl"' in cat
