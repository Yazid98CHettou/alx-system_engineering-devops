#!/usr/bin/python3

import json
import requests as r
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    USR = r.get(URL + "users/{}".format(USER_ID)).json()
    USERNAME = USR.get("username")
    to_do = r.get(URL + "todos", params={"user_id": USER_ID}).json()

    with open("{}.json".format(USER_ID), "w") as jsonfile:
        json.dump({USER_ID: [{"task": e.get("title"),
                              "completed": e.get("completed"),
                              "username": USERNAME} for e in to_do]},
                  jsonfile)
