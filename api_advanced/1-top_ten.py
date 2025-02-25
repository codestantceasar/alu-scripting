#!/usr/bin/python3
# Script to query the Reddit API and print the titles of the first 10
# hot posts for a given subreddit.
import requests


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot posts
    for the given subreddit.
    
    If the subreddit is invalid, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "Python:1-top_ten:v1.0 (by /u/yourusername)"
    }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    data = r.json()
    if "data" in data and "children" in data["data"]:
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 {} subreddit".format(__file__))
    else:
        top_ten(sys.argv[1])
