#!/usr/bin/python3
"""
Function to query the Reddit API and print the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    if "data" in data and "children" in data["data"]:
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
