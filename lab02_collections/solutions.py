"""
Lab 02: Lists, Strings and Dictionaries (model solutions)
Try the exercises yourself before reading these!
"""


def remove_duplicates(items):
    seen = set()  # checking "in" on a set is much faster than on a list
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def second_largest(numbers):
    distinct = sorted(set(numbers), reverse=True)
    if len(distinct) < 2:
        return None
    return distinct[1]


def word_frequency(text):
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def average_scores(records):
    totals = {}
    counts = {}
    for name, score in records:
        totals[name] = totals.get(name, 0) + score
        counts[name] = counts.get(name, 0) + 1
    return {name: round(totals[name] / counts[name], 2) for name in totals}
