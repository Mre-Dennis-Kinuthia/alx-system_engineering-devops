#!/usr/bin/python3

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        articles = data["data"]["children"]
        
        for article in articles:
            title = article["data"]["title"].lower()
            
            for word in word_list:
                count = title.count(word.lower())
                if word.lower() in counts:
                    counts[word.lower()] += count
                else:
                    counts[word.lower()] = count
        
        after = data["data"]["after"]
        
        if after is not None:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Error: Invalid subreddit or unable to fetch data")
