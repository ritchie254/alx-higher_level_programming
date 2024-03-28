#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""
import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.text)
    except Exception as e:
        if req.status_code >= 400:
            print("Error code: {}".format(req.status_code))
