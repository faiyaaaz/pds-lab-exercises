"""Tests for Lab 02. Each test gets the module being checked as `m`."""


def expect(actual, expected, call):
    assert actual == expected, f"{call} returned {actual!r}, expected {expected!r}"


def test_remove_duplicates(m):
    expect(m.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2], "remove_duplicates([3, 1, 3, 2, 1])")
    expect(m.remove_duplicates(["b", "a", "b"]), ["b", "a"], 'remove_duplicates(["b", "a", "b"])')
    expect(m.remove_duplicates([]), [], "remove_duplicates([])")

    original = [1, 1, 2]
    m.remove_duplicates(original)
    assert original == [1, 1, 2], "remove_duplicates changed the original list, return a new one instead"


def test_second_largest(m):
    expect(m.second_largest([10, 40, 30, 40]), 30, "second_largest([10, 40, 30, 40])")
    expect(m.second_largest([-1, -5, -3]), -3, "second_largest([-1, -5, -3])")
    expect(m.second_largest([5, 5]), None, "second_largest([5, 5])")
    expect(m.second_largest([5]), None, "second_largest([5])")


def test_word_frequency(m):
    expect(m.word_frequency("Data is data. Big data!"), {"data": 3, "is": 1, "big": 1},
           'word_frequency("Data is data. Big data!")')
    expect(m.word_frequency("Hello, hello? HELLO"), {"hello": 3}, 'word_frequency("Hello, hello? HELLO")')
    expect(m.word_frequency(""), {}, 'word_frequency("")')


def test_is_palindrome(m):
    expect(m.is_palindrome("Never odd or even"), True, 'is_palindrome("Never odd or even")')
    expect(m.is_palindrome("A man, a plan, a canal: Panama!"), True,
           'is_palindrome("A man, a plan, a canal: Panama!")')
    expect(m.is_palindrome("python"), False, 'is_palindrome("python")')
    expect(m.is_palindrome("12321"), True, 'is_palindrome("12321")')


def test_average_scores(m):
    expect(m.average_scores([("Rafi", 80), ("Mim", 90), ("Rafi", 70)]), {"Rafi": 75.0, "Mim": 90.0},
           'average_scores([("Rafi", 80), ("Mim", 90), ("Rafi", 70)])')
    expect(m.average_scores([("A", 1), ("A", 2), ("A", 2)]), {"A": 1.67},
           'average_scores([("A", 1), ("A", 2), ("A", 2)])')
    expect(m.average_scores([]), {}, "average_scores([])")
