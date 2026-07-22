#!/usr/bin/python3
"""Displays the X-Request-Id header using requests."""

import sys
import requests

response = requests.get(sys.argv[1])
print(response.headers.get("X-Request-Id"))
