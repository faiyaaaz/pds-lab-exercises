"""
Lab 01: Python Basics (model solutions)
Try the exercises yourself before reading these!
"""


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10  # last digit
        n //= 10         # drop the last digit
    return total


def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        # Check 15 first, otherwise 15 would be caught by the "Fizz" branch
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
