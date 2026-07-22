#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                              data={'q': letter})
    try:
        json_body = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not json_body:
            print("No result")
        else:
            print("[{}] {}".format(json_body.get('id'),
                                    json_body.get('name')))
