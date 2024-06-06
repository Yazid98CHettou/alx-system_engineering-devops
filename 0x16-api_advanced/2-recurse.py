import requests

def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            for child in children:
                hot_list.append(child['data']['title'])

            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None
