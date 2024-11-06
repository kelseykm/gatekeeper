import requests
import re
from . import API_KEY

url = "https://api.github.com/user/following"

headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {API_KEY}"
}


def get_all_following_logins() -> list[dict[str, str | int]]:
    all_following = []

    # initial conditions
    parameters = {
        "per_page": "100",
        "page": "1"
    }

    with requests.Session() as sess:
        resp = sess.get(url, headers=headers, params=parameters, timeout=10)
        resp.raise_for_status()

        following = resp.json()

        all_following.extend(following)

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

            following = resp.json()

            all_following.extend(following)

        return sorted([following["login"] for following in all_following])


def unfollow_users(user_logins: list[str]):
    if user_logins:
        with requests.Session() as sess:
            for user_login in user_logins:
                resp = sess.delete(f"{url}/{user_login}",
                                   headers=headers, timeout=10)

                resp.raise_for_status()
                print(f"Unfollowed {user_login}")


def follow_users(user_logins: list[str]):
    if user_logins:
        with requests.Session() as sess:
            for user_login in user_logins:
                resp = sess.put(f"{url}/{user_login}",
                                headers=headers, timeout=10)

                resp.raise_for_status()
                print(f"Followed {user_login}")
