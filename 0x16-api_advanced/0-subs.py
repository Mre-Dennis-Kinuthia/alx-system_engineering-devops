#!/usr/bin/python3
"""
Module to retrieve subscriber count for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of total subscribers of a subreddit
    """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {"User-Agent": "MyUser"}
    response = requests.get(url, allow_redirects=False, headers=header)

    if response.status_code == 404:
        return (0)
    if response.status_code == 200:
        req = int(response.json().get("data").get("subscribers"))
        return (req)
