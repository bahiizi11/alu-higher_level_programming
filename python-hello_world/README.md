# python-hello_world

This directory is part of the `alu-higher_level_programming` repository and
covers the fundamentals of Python: running scripts, printing values, working
with variables, and basic string manipulation, along with a couple of Shell
scripts used to run Python code dynamically.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where the name 'Python' comes from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using `print`
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check code with pycodestyle

## Requirements

* All scripts run on Ubuntu 20.04 LTS using Python 3
* All files end with a new line
* The first line of all Python files is exactly `#!/usr/bin/python3`
* Shell scripts are exactly 2 lines long, starting with `#!/bin/bash`
* Code follows the pycodestyle style guide
* All files are executable (`chmod +x`)
* The length of files is tested using `wc`

## Files

| File | Description |
| --- | --- |
| `0-run` | Shell script that runs a Python script named in `$PYFILE` |
| `1-run_inline` | Shell script that runs Python code stored in `$PYCODE` |
| `2-print.py` | Prints an exact string using `print` |
| `3-print_number.py` | Prints an integer followed by "Battery street" using an f-string |
| `4-print_float.py` | Prints a float with 2 digits of precision using an f-string |
| `5-print_string.py` | Prints a string 3 times, then its first 9 characters |
| `6-concat.py` | Concatenates `str1` and `str2` to print a welcome message |
| `7-edges.py` | Slices a string into its first 3, last 2, and middle characters |
| `8-concat_edges.py` | Builds and prints a new sentence from existing variables |
| `9-easter_egg.py` | Prints the Zen of Python |

## Usage

**Python scripts:**
```bash
./2-print.py
```

**Shell scripts** (require an environment variable to be set first):
```bash
export PYFILE=main.py
./0-run

export PYCODE='print("Hello")'
./1-run_inline
```

## Author

Bahiizi11
