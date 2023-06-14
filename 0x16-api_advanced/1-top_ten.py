#!/usr/bin/python3
"""
Module to print the titles of the first 10 hot posts
listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Retrieves the top 10 hot posts of a subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    header = {"User-Agent": "MyUser"}
    response = requests.get(url, allow_redirects=False, headers=header)

    if response.status_code == 404:
        print(None)
    if response.status_code == 200:
        req = response.json().get("data").get("children")
        for i in range(10):
            print(req[i].get("data").get("title"))
