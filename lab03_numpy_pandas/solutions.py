"""
Lab 03: Intro to NumPy and pandas (model solutions)
Try the exercises yourself before reading these!
"""

import numpy as np
import pandas as pd


def normalize(values):
    spread = values.max() - values.min()
    if spread == 0:
        return np.zeros(len(values))
    return (values - values.min()) / spread  # works on every element at once


def count_above_mean(values):
    # (values > mean) is an array of True/False, and True counts as 1 when summed
    return int((values > values.mean()).sum())


def fill_missing_with_mean(df, column):
    result = df.copy()  # without .copy() we would modify the caller's DataFrame
    result[column] = result[column].fillna(result[column].mean())
    return result


def top_n(df, column, n):
    return df.sort_values(column, ascending=False).head(n).reset_index(drop=True)


def average_by_group(df, group_col, value_col):
    return df.groupby(group_col)[value_col].mean().round(2).to_dict()
