"""Reference answers that can be checked by running code are checked here, not trusted."""
import datetime
import ipaddress
import math
import sqlite3
import unicodedata


def test_aq007_subnet_math():
    net = ipaddress.ip_network("192.168.10.100/26", strict=False)
    assert str(net.network_address) == "192.168.10.64"
    assert str(net.broadcast_address) == "192.168.10.127"
    hosts = list(net.hosts())
    assert len(hosts) == 62 and str(hosts[0]) == "192.168.10.65" and str(hosts[-1]) == "192.168.10.126"


def test_aq011_sql_null_semantics():
    db = sqlite3.connect(":memory:")
    db.execute("create table users (id integer, email text)")
    rows = [(i, f"user{i}@x.com") for i in range(7)] + [(7, None), (8, None), (9, None)]
    db.executemany("insert into users values (?, ?)", rows)
    one = lambda sql: db.execute(sql).fetchone()[0]
    assert one("select count(*) from users where email = NULL") == 0
    assert one("select count(*) from users where email is NULL") == 3
    assert one("select count(email) from users") == 7
    assert one("select count(*) from users where email <> 'a@x.com'") == 7


def test_aq013_float_comparison():
    assert (0.1 + 0.2 == 0.3) is False
    assert repr(0.1 + 0.2) == "0.30000000000000004"
    assert math.isclose(0.1 + 0.2, 0.3)


def test_aq014_mutable_default_argument():
    def add(x, items=[]):
        items.append(x)
        return items
    a = add(1)
    b = add(2)
    c = add(3, [])
    assert (a, b, c, a is b) == ([1, 2], [1, 2], [3], True)


def test_aq015_bool_is_int():
    assert True + True == 2 and isinstance(True, int) and sum([True, False, True]) == 2 and issubclass(bool, int)


def test_aq016_iso_week_of_new_year_2021():
    assert tuple(datetime.date(2021, 1, 1).isocalendar()) == (2020, 53, 5)
    assert datetime.date(2021, 1, 1).strftime("%A") == "Friday"


def test_aq017_unicode_normalization():
    pre, dec = "\u00e9", "e\u0301"
    assert (len(pre), len(pre.encode("utf-8"))) == (1, 2)
    assert (len(dec), len(dec.encode("utf-8"))) == (2, 3)
    assert pre != dec and unicodedata.normalize("NFC", dec) == pre and unicodedata.normalize("NFD", pre) == dec


def test_aq022_year_2038_boundary():
    utc = datetime.timezone.utc
    assert 2**31 - 1 == 2147483647
    assert datetime.datetime.fromtimestamp(2147483647, tz=utc) == datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=utc)
    try:
        assert datetime.datetime.fromtimestamp(-2147483648, tz=utc) == datetime.datetime(1901, 12, 13, 20, 45, 52, tzinfo=utc)
    except OSError:
        # negative epoch timestamps raise OSError on Windows; supported on Linux/CI
        pass


def test_aq024_boundary_values():
    lo, hi = 18, 65
    assert [lo - 1, lo, hi, hi + 1] == [17, 18, 65, 66]
    assert [lo - 1, lo, lo + 1, hi - 1, hi, hi + 1] == [17, 18, 19, 64, 65, 66]
