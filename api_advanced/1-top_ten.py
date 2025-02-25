#!/usr/bin/python3
"""
Module: 1-top_ten
Description:
    This module defines the function 'top_ten' that queries the Reddit API 
    to retrieve the top 10 hot posts for a given subreddit and prints their titles.
    
    If the subreddit is invalid (or a redirect occurs), the function prints None.
    
Usage:
    Import and call the function:
        from 1-top_ten import top_ten
        top_ten("programming")
        
    Or run the module as a script:
        $ python3 1-top_ten.py programming

    In the latter case, the script expects a single command-line argument
    representing the subreddit to query.

Requirements:
    - The 'requests' library must be installed (install it using 'pip install requests').
    
Notes:
    - A custom User-Agent header is used to ensure proper responses from the API.
    - Redirects are disabled (allow_redirects=False) to properly catch invalid subreddits.
    
Example:
    $ python3 1-top_ten.py programming
    Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
    How a 64k intro is made
    HTTPS on Stack Overflow: The End of a Long Road
    Spend effort on your Git commits
    It's a few years old, but I just discovered this incredibly impressive video of 
    researchers reconstructing sounds from video information alone
    From the D Blog: Introspection, Introspection Everywhere
    Do MVC like it’s 1979
    GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
    Google Bug Bounty - The 5k Error Page
    PyCon 2017 Talk Videos

Author:
    Your Name or GitHub username
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API for the top 10 hot posts of a given subreddit and
    prints the title of each post.

    Parameters:
        subreddit (str): The name of the subreddit to query.

    Behavior:
        - If the subreddit is valid, prints the titles of the top 10 hot posts.
        - If the subreddit is invalid (or causes a redirect), prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Python:1-top_ten:v1.0 (by /u/yourusername)"}
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
