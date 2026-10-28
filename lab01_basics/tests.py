"""Tests for Lab 01. Each test gets the module being checked as `m`."""


def expect(actual, expected, call):
    assert actual == expected, f"{call} returned {actual!r}, expected {expected!r}"


def test_celsius_to_fahrenheit(m):
    expect(m.celsius_to_fahrenheit(0), 32, "celsius_to_fahrenheit(0)")
    expect(m.celsius_to_fahrenheit(100), 212, "celsius_to_fahrenheit(100)")
    expect(m.celsius_to_fahrenheit(-40), -40, "celsius_to_fahrenheit(-40)")
    expect(m.celsius_to_fahrenheit(37.5), 99.5, "celsius_to_fahrenheit(37.5)")


def test_is_leap_year(m):
    expect(m.is_leap_year(2024), True, "is_leap_year(2024)")
    expect(m.is_leap_year(2023), False, "is_leap_year(2023)")
    expect(m.is_leap_year(1900), False, "is_leap_year(1900)")
    expect(m.is_leap_year(2000), True, "is_leap_year(2000)")


def test_sum_of_digits(m):
    expect(m.sum_of_digits(4096), 19, "sum_of_digits(4096)")
    expect(m.sum_of_digits(7), 7, "sum_of_digits(7)")
    expect(m.sum_of_digits(0), 0, "sum_of_digits(0)")
    expect(m.sum_of_digits(1000), 1, "sum_of_digits(1000)")


def test_fizzbuzz(m):
    expect(m.fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"], "fizzbuzz(5)")
    expect(m.fizzbuzz(15)[-1], "FizzBuzz", "fizzbuzz(15)[-1]")
    expect(len(m.fizzbuzz(30)), 30, "len(fizzbuzz(30))")
    expect(m.fizzbuzz(0), [], "fizzbuzz(0)")


def test_count_vowels(m):
    expect(m.count_vowels("Data Science"), 5, 'count_vowels("Data Science")')
    expect(m.count_vowels("AEIOU"), 5, 'count_vowels("AEIOU")')
    expect(m.count_vowels("rhythm"), 0, 'count_vowels("rhythm")')
    expect(m.count_vowels(""), 0, 'count_vowels("")')
