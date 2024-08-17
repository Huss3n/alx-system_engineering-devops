import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'
    }

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            subs = data.get("data", {}).get("subscribers", 0)
            return subs
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0


# Example usage
# subscribers = number_of_subscribers("learnpython")
# print(f"Subscribers: {subscribers}")
