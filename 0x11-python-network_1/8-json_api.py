#!/usr/bin/python3
"""
Python script that takes in a letter and sends a rrquest
"""

import sys
import requests

if __name__ == "__main__":
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json_file = req.json()
        if json_file:
            print("[{}] {}".format(json_file.get("id"), json_file.get("name")))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
