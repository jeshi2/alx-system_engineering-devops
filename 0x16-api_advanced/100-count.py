#!/usr/bin/pyhthon3
"""
recursive function that queries the Reddit API, 
parses the title of all hot articles, and prints a 
sorted count of given keywords (case-insensitive, 
delimited by spaces. Javascript should count as 
javascript, but java should not).
"""

import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively query the Reddit API, parse hot article 
    titles, and count specified keywords.
    """
    if word_count is None:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/1.0 (by YourUsername)'}  # Use a custom User-Agent header
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    if f' {word} ' in f' {title} ':
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1

            after = data['data']['after']
            if after is not None:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return None  # Subreddit doesn't exist or some other issue
    except Exception as e:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        keywords = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, keywords)
