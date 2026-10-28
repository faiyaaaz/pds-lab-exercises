# Programming for Data Science: Lab Exercises

Practice problems for an introductory **Python for Data Science** lab. The set includes three labs with five problems each. A checker gives instant feedback on every problem, so students know right away what works and what to fix.

| Lab | Topics | Problems |
|---|---|---|
| [Lab 01: Basics](lab01_basics/exercises.py) | variables, if/else, loops, strings | Celsius to Fahrenheit, leap year, sum of digits, FizzBuzz, count vowels |
| [Lab 02: Collections](lab02_collections/exercises.py) | lists, strings, dictionaries | remove duplicates, second largest, word frequency, palindrome, average scores |
| [Lab 03: NumPy & pandas](lab03_numpy_pandas/exercises.py) | arrays, DataFrames, missing values, groupby | normalize, count above mean, fill missing, top N rows, average by group |

## How to use

1. Open a lab's `exercises.py` and read the problem in each function's docstring.
2. Replace `raise NotImplementedError` with your code.
3. Check your answers:

```bash
python check.py lab01
```

```
Checking lab01_basics/exercises.py

  [PASS]  celsius_to_fahrenheit
  [FAIL]  is_leap_year: is_leap_year(1900) returned True, expected False
  [PASS]  sum_of_digits
  [FAIL]  fizzbuzz: fizzbuzz(5) returned ['1', '2', '3', '4', '5'], expected ['1', '2', 'Fizz', '4', 'Buzz']
  [TODO]  count_vowels: not attempted yet

2/5 passed. Keep going!
```

A failed check shows the exact input you got wrong, which makes it easy to debug. Model solutions are in each lab's `solutions.py`. Try the problems yourself first! To confirm the solutions pass, run `python check.py lab01 --solutions`.

**Requirements:** Python 3.9+. Lab 03 also needs `pip install numpy pandas`.

## Common mistakes to watch for

These are the mistakes I'd expect to see most often in each lab, and the tests check for them on purpose.

**Lab 01**
- **FizzBuzz order:** checking `% 3` before `% 15` means 15 prints `"Fizz"` instead of `"FizzBuzz"`.
- **Leap years:** `year % 4 == 0` alone is wrong for 1900. Century years need the extra rule.
- **`print` vs `return`:** a function that prints its answer returns `None`, so the checker sees `None`.
- **Uppercase letters:** `"A"` is not in `"aeiou"`. Convert with `.lower()` first.

**Lab 02**
- **Changing the input list:** `items.remove(...)` inside a loop over `items` skips elements and changes the caller's list.
- **Duplicates in second largest:** `sorted(nums)[-2]` gives 40 for `[10, 40, 30, 40]`. Remove duplicates first.
- **Punctuation:** `"data."` and `"data"` count as different words unless you strip the `.`.

**Lab 03**
- **Writing loops:** `for x in arr:` works, but `(arr - arr.min()) / ...` is shorter and much faster. That's the point of NumPy.
- **Dividing by zero:** an array where every value is the same has `max - min == 0`.
- **Forgetting `.copy()`:** changing a DataFrame inside a function also changes the caller's DataFrame.
- **Leftover index:** after `sort_values`, the index keeps the old row numbers until you call `reset_index(drop=True)`.

## Adding a new lab

Create a folder `labNN_topic/` with three files:
- `exercises.py`: function stubs with docstrings
- `solutions.py`: the model answers
- `tests.py`: functions named `test_<problem>(m)` that check `m.<problem>(...)` with `assert`

`check.py` finds the tests automatically.
