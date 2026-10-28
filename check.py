"""
Checks your answers for a lab and tells you which ones are right.

Usage:
    python check.py lab01                # check your answers in exercises.py
    python check.py lab01 --solutions    # check the model solutions instead
"""

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def load_module(path):
    """Import a .py file by its path."""
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_lab(name):
    """Accept 'lab01', '01' or the full folder name 'lab01_basics'."""
    if not name.startswith("lab"):
        name = "lab" + name.zfill(2)
    matches = sorted(p for p in ROOT.glob(name + "*") if p.is_dir())
    if not matches:
        raise SystemExit(f"No lab folder matching '{name}'. Try: lab01, lab02 or lab03.")
    return matches[0]


def main():
    parser = argparse.ArgumentParser(description="Check your lab answers.")
    parser.add_argument("lab", help="which lab to check, e.g. lab01")
    parser.add_argument("--solutions", action="store_true", help="check solutions.py instead")
    args = parser.parse_args()

    lab_dir = find_lab(args.lab)
    answer_file = lab_dir / ("solutions.py" if args.solutions else "exercises.py")
    print(f"Checking {answer_file.relative_to(ROOT)}\n")

    answers = load_module(answer_file)
    tests = load_module(lab_dir / "tests.py")

    passed = 0
    test_functions = [f for name, f in vars(tests).items() if name.startswith("test_")]
    for test in test_functions:
        label = test.__name__.removeprefix("test_")
        try:
            test(answers)
        except NotImplementedError:
            print(f"  [TODO]  {label}: not attempted yet")
        except AssertionError as error:
            print(f"  [FAIL]  {label}: {error}")
        except Exception as error:
            print(f"  [ERROR] {label}: your code crashed with {type(error).__name__}: {error}")
        else:
            print(f"  [PASS]  {label}")
            passed += 1

    total = len(test_functions)
    print(f"\n{passed}/{total} passed.", "Great work!" if passed == total else "Keep going!")
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
