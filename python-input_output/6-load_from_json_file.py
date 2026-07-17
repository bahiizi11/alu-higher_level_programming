#!/usr/bin/python3
"""Module that defines a function to create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename: the path of the JSON file to read

    Returns:
        The Python data structure represented by the file's content
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
