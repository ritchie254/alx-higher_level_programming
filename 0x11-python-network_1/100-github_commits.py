#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challeng
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/"
    url += owner + '/' + repo + '/commits'
    req = requests.get(url)
    for i in range(len(req.json())):
        data1 = req.json()[i].get("sha")
        commit = req.json()[i].get("commit").get("committer").get("name")
        print("{}: {}".format(data1, commit))
