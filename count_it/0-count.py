#!/usr/bin/python3
"""
Defines recursive function to query the Reddit API,
parse titles of all hot articles, and print sorted count
"""


def count_words(subreddit, word_list, after=None, count=None):
    """
    Queries the Reddit API, parses titles of all hot articles,
    and prints sorted count

    parameters:
        subreddit: subreddit to query for hot articles
        word_list: list of keywords to count
        after: indicates next starting point to get data after
        count: dictionary of current count of keyword
    """
    import json
    import requests

    if count is None:
        count = {}

    if after is None:
        sub_URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        sub_URL = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)

    try:
        subreddit_info = requests.get(sub_URL,
                                      headers={"user-agent": "user"},
                                      allow_redirects=False)
        # Raise an HTTPError for bad responses
        subreddit_info.raise_for_status()
        data = subreddit_info.json().get("data")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"JSON decode failed: {e}")
        return

    for word in word_list:
        word = word.lower()
        if word not in count:
            count[word] = 0

    children = data.get("children")
    for child in children:
        title = child.get("data", {}).get("title", "").lower()
        title_words = title.split(' ')
        for word in word_list:
            word = word.lower()
            count[word] += title_words.count(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, count)

    result = []
    for k in count:
        if count[k] != 0:
            if not result:
                result.append("{}: {}".format(k, count[k]))
            else:
                inserted = False
                for i in range(len(result)):
                    if count[k] > int(result[i].split(' ')[1]):
                        result = (result[:i]
                                  + ["{}: {}".format(k, count[k])]
                                  + result[i:])
                        inserted = True
                        break
                    elif count[k] == int(result[i].split(' ')[1]):
                        alpha_list = [k, result[i].split(' ')[0]]
                        j = 1
                        while i + j < len(result) and \
                                count[k] == int(result[i + j].split(' ')[1]):
                            alpha_list.append(result[i + j].split(' ')[0])
                            j += 1
                        alpha_list.sort()
                        for j in range(len(alpha_list)):
                            if k == alpha_list[j]:
                                result = (
                                    result[:i + j]
                                    + ["{}: {}".format(k, count[k])]
                                    + result[i + j:])
                                inserted = True
                                break
                if not inserted:
                    result.append("{}: {}".format(k, count[k]))

    if result:
        for printing in result:
            print(printing)
