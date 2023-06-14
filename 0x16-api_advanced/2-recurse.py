#!/usr/bin/python3
"""
Module to return a list of the titles of all hot posts
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], params={}):
    """
    Returns a list of titles of all hot posts of a subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    header = {"User-Agent": "MyUser"}

    response = requests.get(url, allow_redirects=False,
                            headers=header, params=params)
    data = response.json().get("data")

    if response.status_code == 404:
        return(None)

    after = data.get("after")
    before = data.get("before")

    if response.status_code == 200:
        req = data.get("children")
        for item in req:
            hot_list.append(item.get("data").get("title"))

    if after is None:
        return(hot_list)

    return recurse(subreddit, hot_list,
                   params={"after": after, "before": before})
