"""Tests for Lab 03. Each test gets the module being checked as `m`."""

import numpy as np
import pandas as pd


def expect(actual, expected, call):
    assert actual == expected, f"{call} returned {actual!r}, expected {expected!r}"


def test_normalize(m):
    result = m.normalize(np.array([10, 20, 30]))
    assert np.allclose(result, [0, 0.5, 1]), f"normalize([10, 20, 30]) returned {result}, expected [0, 0.5, 1]"

    result = m.normalize(np.array([5.0, -5.0, 0.0]))
    assert np.allclose(result, [1, 0, 0.5]), f"normalize([5, -5, 0]) returned {result}, expected [1, 0, 0.5]"

    result = m.normalize(np.array([7, 7, 7]))
    assert np.allclose(result, [0, 0, 0]), f"normalize([7, 7, 7]) returned {result}, expected [0, 0, 0]"


def test_count_above_mean(m):
    expect(m.count_above_mean(np.array([1, 2, 3, 10])), 1, "count_above_mean([1, 2, 3, 10])")
    expect(m.count_above_mean(np.array([1, 2, 3, 4])), 2, "count_above_mean([1, 2, 3, 4])")
    expect(m.count_above_mean(np.array([5, 5, 5])), 0, "count_above_mean([5, 5, 5])")
    assert isinstance(m.count_above_mean(np.array([1, 2])), int), "count_above_mean should return an int"


def test_fill_missing_with_mean(m):
    df = pd.DataFrame({"name": ["A", "B", "C"], "marks": [80, None, 60]})
    result = m.fill_missing_with_mean(df, "marks")
    expect(result["marks"].tolist(), [80.0, 70.0, 60.0], "fill_missing_with_mean(...)['marks']")
    assert df["marks"].isna().sum() == 1, "the original DataFrame was changed, work on a copy instead"


def test_top_n(m):
    df = pd.DataFrame({"name": ["A", "B", "C", "D"], "cgpa": [3.2, 3.9, 3.5, 2.8]})
    result = m.top_n(df, "cgpa", 2)
    expect(result["name"].tolist(), ["B", "C"], "top_n(df, 'cgpa', 2)['name']")
    expect(result.index.tolist(), [0, 1], "top_n(df, 'cgpa', 2).index (did you reset the index?)")
    expect(len(m.top_n(df, "cgpa", 10)), 4, "len(top_n(df, 'cgpa', 10))")


def test_average_by_group(m):
    df = pd.DataFrame({"dept": ["CSE", "DS", "CSE", "DS", "EEE"],
                       "cgpa": [3.0, 3.6, 3.5, 3.2, 3.33]})
    expect(m.average_by_group(df, "dept", "cgpa"), {"CSE": 3.25, "DS": 3.4, "EEE": 3.33},
           "average_by_group(df, 'dept', 'cgpa')")
