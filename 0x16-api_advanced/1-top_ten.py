import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            children = data.get('children', [])
            if not children:
                print("None")
                return
            for child in children:
                print(child['data']['title'])
        else:
            print("None")
    except Exception as e:
        print("None")
