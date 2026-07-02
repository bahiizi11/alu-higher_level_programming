#!/usr/bin/python3
"""Prints all the names defined by the compiled module hidden_4.pyc
that do not start with __, one per line, in alphabetical order
"""
import hidden_4

if __name__ == "__main__":
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)
