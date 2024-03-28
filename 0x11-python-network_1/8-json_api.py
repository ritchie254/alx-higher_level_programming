#!/usr/bin/python3
"""
Python script that takes in a letter and sends a rrquest
"""

import sys
import requests
import json


def searchLetter(letter):
    """
    Python script that takes in a letter and sends a POST request
    """
    if not letter:
        letter = ""
    req = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        data = req.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    searchLetter(letter)
