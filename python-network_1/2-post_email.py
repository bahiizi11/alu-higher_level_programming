#!/usr/bin/python3
"""Sends a POST request with an email."""

import sys
from urllib import request, parse

data = parse.urlencode({"email": sys.argv[2]}).encode("utf-8")

with request.urlopen(sys.argv[1], data=data) as response:
    print(response.read().decode("utf-8"))
