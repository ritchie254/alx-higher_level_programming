#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status

    You must use the package urllib
"""
import urllib.request

if __name__ == "__main__":
    res = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(res) as response:
        value = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(value)))
        print("\t- content: {}".format(value))
        print("\t- utf8 content: {}".format(value.decode('utf-8')))
