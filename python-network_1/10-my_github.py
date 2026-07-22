#!/usr/bin/python3
"""Takes GitHub credentials (username, password/personal access token)
and uses the GitHub API to display the user's id"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get("https://api.github.com/user",
                             auth=(username, password))
    print(response.json().get('id'))
