"""
Lab 02: Lists, Strings and Dictionaries
Topics: list methods, string methods, dictionaries, looping over collections

Replace each `raise NotImplementedError` with your own code, then run:
    python check.py lab02
"""


def remove_duplicates(items):
    """
    Return a new list with duplicates removed, keeping the FIRST time each item appears.
    Do not change the original list.

    >>> remove_duplicates([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    raise NotImplementedError


def second_largest(numbers):
    """
    Return the second largest DISTINCT number in the list.
    Return None if there is no second largest (e.g. [5] or [5, 5]).

    >>> second_largest([10, 40, 30, 40])
    30
    """
    raise NotImplementedError


def word_frequency(text):
    """
    Return a dictionary counting how many times each word appears.
    Ignore case, and strip the punctuation marks . , ! ? from the words.

    >>> word_frequency("Data is data. Big data!")
    {'data': 3, 'is': 1, 'big': 1}
    """
    raise NotImplementedError


def is_palindrome(text):
    """
    Return True if `text` reads the same forwards and backwards,
    ignoring case, spaces and punctuation (keep only letters and digits).

    >>> is_palindrome("Never odd or even")
    True
    """
    raise NotImplementedError


def average_scores(records):
    """
    `records` is a list of (name, score) tuples. A name can appear many times.
    Return a dictionary of each name's average score, rounded to 2 decimal places.

    >>> average_scores([("Rafi", 80), ("Mim", 90), ("Rafi", 70)])
    {'Rafi': 75.0, 'Mim': 90.0}
    """
    raise NotImplementedError
