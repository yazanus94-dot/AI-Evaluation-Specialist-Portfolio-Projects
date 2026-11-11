"""Claims marked executed_locally are reproduced here, not trusted."""
import sqlite3


def test_sorted_is_stable():
    records = [("b", 1), ("a", 1), ("d", 0), ("c", 1), ("e", 0)]
    result = sorted(records, key=lambda r: r[1])
    assert result == [("d", 0), ("e", 0), ("b", 1), ("a", 1), ("c", 1)]


def test_list_sort_is_stable():
    records = [("b", 1), ("a", 1), ("d", 0), ("c", 1), ("e", 0)]
    records.sort(key=lambda r: r[1])
    assert [r[0] for r in records] == ["d", "e", "b", "a", "c"]


def test_is_compares_identity_not_equality():
    a, b = [1, 2, 3], [1, 2, 3]
    assert a == b and a is not b


def test_floor_division_rounds_down():
    assert -7 // 2 == -4 and divmod(-7, 2) == (-4, 1) and int(-7 / 2) == -3


def test_non_empty_string_is_truthy():
    assert bool("False") is True and bool("") is False


def test_tuple_can_hold_mutable_objects():
    t = (1, [2, 3])
    t[1].append(4)
    assert t == (1, [2, 3, 4])
    try:
        t[0] = 9
    except TypeError:
        return
    raise AssertionError("tuple item assignment should fail")


def test_round_half_to_even():
    assert round(2.5) == 2 and round(3.5) == 4 and round(0.5) == 0


def test_sqlite_supports_drop_column():
    if sqlite3.sqlite_version_info < (3, 35, 0):
        return  # older SQLite: the claim "not supported" would be true on this build
    db = sqlite3.connect(":memory:")
    db.execute("create table t (a integer, b text)")
    db.execute("alter table t drop column b")
    assert [row[1] for row in db.execute("pragma table_info(t)")] == ["a"]


def test_float_sum_is_not_exact():
    assert (0.1 + 0.2 == 0.3) is False and repr(0.1 + 0.2) == "0.30000000000000004"


def test_bool_is_int_subclass():
    assert issubclass(bool, int) and True + True == 2
