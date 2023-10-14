#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns 
a list containing the titles of all hot articles for a given 
subreddit. If no results are found for the given subreddit, 
the function should return None.
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query the Reddit API to collect the 
    titles of all hot posts for a subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0 (by YourUsername)'} 
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None  
    except Exception as e:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
