# CLAUDE.md — Coursera Python Learning Repository

## Overview

This repository contains Python exercises from the **"Python for Everybody"** (py4e) course, based on the textbook by Dr. Charles Severance. The course material is in Dutch (the learner's language), so commit messages and some variable names appear in Dutch.

## Repository Structure

```
Coursera/
├── ex_XX_YY.py         # Official course exercises (chapter XX, exercise YY)
├── ex_book_6_X.py      # Textbook exercises from chapter 6
├── H7.py               # Chapter 7 scratch/practice file
├── test.py             # Quick test/scratch script
├── test_boek.py        # Textbook example for testing
├── mbox.txt            # Full email dataset (used in ch. 7 exercises)
├── mbox-short.txt      # Short email dataset (used in ch. 7 exercises)
├── words.txt           # Word list (referenced in textbook examples)
└── Materiaal/          # Course slides (.pptx) and textbook PDF
    ├── Pythonlearn-01-Intro.pptx
    ├── Pythonlearn-02-Expressions.pptx
    ├── Pythonlearn-03-Conditional.pptx
    ├── Pythonlearn-04-Functions.pptx
    ├── Pythonlearn-05-Iterations.pptx
    ├── Pythonlearn-06-Strings.pptx
    ├── Pythonlearn-07-Files.pptx
    ├── Pythonlearn-08-Lists.pptx
    └── pythonlearn.pdf
```

## Exercise File Naming Convention

| Pattern | Chapter | Topic |
|---|---|---|
| `ex_02_XX.py` | 2 | Expressions & basic I/O |
| `ex_03_XX.py` | 3 | Conditionals |
| `ex_04_XX.py` | 4 | Functions |
| `ex_05_XX.py` | 5 | Iterations / loops |
| `ex_06_XX.py` | 6 | Strings |
| `ex_book_6_X.py` | 6 | Textbook string exercises |
| `ex_07_XX.py` | 7 | File I/O |

## Known Bugs / Learning Notes

These files contain intentional or unintentional bugs that are part of the learning process. Do not silently "fix" them unless the learner asks:

- **`ex_03_02.py`**: Variable `xp` is assigned but printed as `XP` (case mismatch) — this will raise a `NameError` at runtime.
- **`ex_book_6_3.py`**: Uses `count` inside a function without declaring it `global` — will raise `UnboundLocalError`. This is a common scoping pitfall covered in ch. 4–5.

## Data Files

- **`mbox-short.txt`** / **`mbox.txt`**: Real email mbox archives from the Sakai project, used in chapter 7 file-reading exercises. `mbox-short.txt` is a small subset suitable for quick testing; `mbox.txt` is the full dataset.
- **`words.txt`**: Excerpt from the py4e textbook, used in string/file exercises.

## Development Conventions

- **Language**: Python 3 (no shebangs or version pins present; assume standard system Python 3).
- **Style**: Exercises are intentionally simple and beginner-level. Do not refactor to add classes, type hints, list comprehensions, or other advanced constructs unless explicitly asked.
- **Variable names**: Mix of English and Dutch is expected (e.g., `antwoord` = "answer", `oefening` = "exercise"). Preserve the learner's style.
- **No dependencies**: All exercises use the Python standard library only. Do not introduce third-party packages.
- **No test framework**: There are no automated tests. `test.py` and `test_boek.py` are manual scratch files, not pytest/unittest suites.

## Commit Message Convention

Commit messages follow a Dutch-language descriptive style matching the existing history:

```
Oefeningen hoofdstuk X        # "Exercises chapter X"
oefening XX_YY                # "exercise XX_YY"
Toevoegen materiaal           # "Adding material"
aanpassing XX_YY              # "adjustment/fix XX_YY"
```

Match this style when committing on behalf of the learner.

## Running Exercises

Most exercises are interactive (they call `input()`). Run them directly:

```bash
python3 ex_07_02.py
# When prompted: Enter file name: mbox-short.txt
```

For file exercises (`ex_07_XX.py`, `H7.py`), the working directory must contain the relevant data files (`mbox.txt`, `mbox-short.txt`, `words.txt`).

## Git Workflow

- Primary branch: `master`
- Feature/AI branches: `claude/<description>-<id>`
- No CI/CD, no pre-commit hooks, no linting pipeline.

## Guidance for AI Assistants

1. **Preserve learning intent**: This is a learning repo. Pointing out bugs is helpful; silently rewriting broken exercises is not.
2. **Keep it simple**: Match the beginner style. Avoid introducing abstractions the learner hasn't encountered yet (e.g., f-strings, `with` statements, list comprehensions) unless the chapter being worked on covers them.
3. **Dutch context**: Comments and commit messages in Dutch are correct and intentional.
4. **No new files by default**: Exercises map 1-to-1 with course assignments. Don't create extra utility modules.
5. **Data files are read-only**: `mbox.txt`, `mbox-short.txt`, and `words.txt` are course-provided datasets — do not modify them.
