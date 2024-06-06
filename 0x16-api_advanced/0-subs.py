#!/usr/bin/python3
import requests
from sys import argv


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Yony'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == requests.codes.ok:
        res_json = res.json()
        subscribers = res_json['data']['subscribers']
    else:
        subscribers = 0
    return subscribers
