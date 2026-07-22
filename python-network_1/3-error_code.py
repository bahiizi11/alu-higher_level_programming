#!/usr/bin/python3
"""Handles HTTP errors."""

import sys
from urllib import request, error

try:
    with request.urlopen(sys.argv[1]) as response:
        print(response.read().decode("utf-8"))
except error.HTTPError as e:
    print("Error code: {}".format(e.code))
