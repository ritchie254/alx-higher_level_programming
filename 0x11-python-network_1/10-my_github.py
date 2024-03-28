#!/usr/bin/python3
"""
Python script that takes your GitHub credentials 
"""

import requests
import sys

if __name__ == "__main__":
    userName = sys.argv[1]
    passWord = sys.argv[2]

    req = requests.get("https://api.github.com/user", auth=(userName, passWord))
    print(req.json().get("id"))
