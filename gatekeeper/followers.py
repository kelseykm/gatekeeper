import requests
import re
from . import API_KEY

url = "https://api.github.com/user/followers"

headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {API_KEY}"
}


def get_all_followers_logins() -> list[dict[str, str | int]]:
    all_followers = []

    # initial conditions
    parameters = {
        "per_page": "100",
        "page": "1"
    }

    with requests.Session() as sess:
        resp = sess.get(url, headers=headers, params=parameters, timeout=10)
        resp.raise_for_status()

        followers = resp.json()

        all_followers.extend(followers)

        while "Link" in resp.headers:
            link_header = resp.headers["Link"]
            if not re.search(r'rel="next"', link_header):
                break

            next_link_full = [*filter(lambda link: re.search(
                r'rel="next"', link), link_header.split(","))]

            next_link = (re.match(r'\<(?P<next>.+?)\>',
                                  next_link_full[0])).group("next")

            resp = sess.get(next_link, headers=headers, timeout=10)
            resp.raise_for_status()

            followers = resp.json()

            all_followers.extend(followers)

        return sorted([follower["login"] for follower in all_followers])
