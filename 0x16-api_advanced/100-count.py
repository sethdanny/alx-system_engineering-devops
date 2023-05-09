#!/usr/bin/python3
""" fetch data from Reddit api """

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""
    if not word_count:
        word_count = {word: 0 for word in word_list}

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit),
                            params={"after": after},
                            headers={"User-Agent": "nadduli daniel"},
                            allow_redirects=False)

    if sub_info.status_code != 200:
        return None

    info = sub_info.json()

    hot_l = [child.get("data").get("title")
             for child in info.get("data").get("children")]
    if not hot_l:
        return None

    for title in hot_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not info.get("data").get("after"):
        sorted_counts = sorted(
            word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in sorted_counts:
            if v != 0:
                print('{}: {}'.format(k, v))
    else:
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
