#!/usr/bin/python3
"""
This module provides a function to query the Reddit API 
and retrieve the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API to get the number of subscribers for a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0 (by YourUsername)'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
