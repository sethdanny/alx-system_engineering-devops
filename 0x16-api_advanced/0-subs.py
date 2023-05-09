#!/usr/bin/python3
""" fetch number of subscribers from reddit api """

import requests


def number_of_subscribers(subreddit):
    """ function to fetch number of subscribers """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "nadduli daniel"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return 0
