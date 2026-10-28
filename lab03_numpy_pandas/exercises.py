"""
Lab 03: Intro to NumPy and pandas
Topics: arrays, vectorized operations, DataFrames, missing values, sorting, groupby

Try to solve these WITHOUT writing a for loop. NumPy and pandas can do it for you!
Replace each `raise NotImplementedError` with your own code, then run:
    python check.py lab03
"""

import numpy as np
import pandas as pd


def normalize(values):
    """
    Min-max scale a NumPy array so the smallest value becomes 0 and the largest becomes 1.
    Formula: (x - min) / (max - min)
    If all values are the same, return an array of zeros (avoid dividing by zero!).

    >>> normalize(np.array([10, 20, 30]))
    array([0. , 0.5, 1. ])
    """
    raise NotImplementedError


def count_above_mean(values):
    """
    Return how many values in the NumPy array are strictly greater than the mean, as an int.

    >>> count_above_mean(np.array([1, 2, 3, 10]))
    1
    """
    raise NotImplementedError


def fill_missing_with_mean(df, column):
    """
    Return a COPY of the DataFrame where missing values (NaN) in `column`
    are replaced by that column's mean. The original DataFrame must not change.

    >>> df = pd.DataFrame({"marks": [80, None, 60]})
    >>> fill_missing_with_mean(df, "marks")["marks"].tolist()
    [80.0, 70.0, 60.0]
    """
    raise NotImplementedError


def top_n(df, column, n):
    """
    Return the `n` rows with the highest values in `column`, sorted from highest to lowest,
    with the index reset to 0, 1, 2, ...

    >>> df = pd.DataFrame({"name": ["A", "B", "C"], "cgpa": [3.2, 3.9, 3.5]})
    >>> top_n(df, "cgpa", 2)["name"].tolist()
    ['B', 'C']
    """
    raise NotImplementedError


def average_by_group(df, group_col, value_col):
    """
    Return a dictionary of the mean of `value_col` for each group in `group_col`,
    rounded to 2 decimal places.

    >>> df = pd.DataFrame({"dept": ["CSE", "DS", "CSE"], "cgpa": [3.0, 3.6, 3.5]})
    >>> average_by_group(df, "dept", "cgpa")
    {'CSE': 3.25, 'DS': 3.6}
    """
    raise NotImplementedError
