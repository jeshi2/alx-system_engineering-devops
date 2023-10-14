#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles 
of the first 10 hot posts listed for a given subreddit.
"""
import requests
import sys

def top_ten(subreddit):
    """
    Query the Reddit API to print the titles of the 
    first 10 hot posts for a subreddit.

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0 (by YourUsername)'} 

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for i, post in enumerate(posts[:10]):
                print(f"{i+1}. {post['data']['title']}")
        else:
            print("None")
    except Exception as e:
        print("None")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
