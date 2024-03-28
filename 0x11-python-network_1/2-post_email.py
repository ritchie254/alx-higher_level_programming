#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = dict()
    data["email"] = sys.argv[2]
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        value = response.read()
        print("{}".format(value.decode('utf-8')))
