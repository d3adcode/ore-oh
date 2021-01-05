from statistics import __version__
from statistics.model import stats, resolve_stats, resolve_add_stat, Statistic

import jsons
import pytest


def test_version():
    assert __version__ == '0.1.0'


def test_resolve_stats():
    assert len(resolve_stats(None, None)) == 0


def test_resolve_add_stat():
    expectedStat = Statistic("id", "source", "stat_id",
                             '{"test":"test"}', "2021-1-1")
    returnStat = resolve_add_stat(None, None, "id",
                                  "source", "stat_id", '{"test":"test"}', "2021-1-1")
    expectList = [expectedStat]
    returnList = resolve_stats(None, None)
    assert (expectedStat, expectList) == (returnStat, returnList)
