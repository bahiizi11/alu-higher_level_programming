#!/usr/bin/python3
"""Takes in a URL, sends a request and displays the body of the
response. If the status code is >= 400, displays an error message"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
