#!/usr/bin/python3
"""
Python script that takes your GitHub
"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]

    req = requests.get("https://api.github.com/user", auth=(user, passw))
    print(req.json().get("id"))
