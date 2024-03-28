#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.getheader("X-Request-Id"))
