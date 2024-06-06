#!/usr/bin/python3
import requests
from sys import argv


def top_ten(subreddit):
    """ get top 10 list reddits """
    headers = {'User-Agent': 'Yony'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == requests.codes.ok:
        cnt = 0
        res_json = res.json()
        for subr in res_json['data']['children']:
            if cnt < 10:
                print(subr['data']['title'])
                cnt += 1
    else:
        print('None')
