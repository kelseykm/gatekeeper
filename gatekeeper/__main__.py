from .arguments import main as arguments
from .followers import get_all_followers_logins
from .following import get_all_following_logins, follow_users, unfollow_users
import tomllib
from pathlib import Path
import os.path

current_file_path = Path(__file__)
config_file_path = os.path.join(current_file_path.parent.parent, "config.toml")


def get_crooks_logins(all_followers_logins: list['str'], all_following_logins: list[str]) -> list[str]:
    crooks = set(all_following_logins).difference(all_followers_logins)

    with open(config_file_path, "rb") as config_file:
        config = tomllib.load(config_file)

    crook_exceptions = config["users"]["exceptions"]["crooks"]

    crooks.difference_update(crook_exceptions)

    return sorted(crooks)


def get_niceys_logins(all_followers_logins: list['str'], all_following_logins: list[str]) -> list[str]:
    niceys = set(all_followers_logins).difference(all_following_logins)

    with open(config_file_path, "rb") as config_file:
        config = tomllib.load(config_file)

    niceys_exceptions = config["users"]["exceptions"]["niceys"]

    niceys.difference_update(niceys_exceptions)

    return sorted(niceys)


def run():
    args = arguments()

    match args:
        case args if args.list_followers:
            all_followers_logins = get_all_followers_logins()

            print(all_followers_logins)

        case args if args.list_following:
            all_following_logins = get_all_following_logins()

            print(all_following_logins)

        case args if args.list_crooks:
            all_followers_logins = get_all_followers_logins()
            all_following_logins = get_all_following_logins()

            crooks = get_crooks_logins(
                all_followers_logins, all_following_logins)

            print(crooks)

        case args if args.unfollow_crooks:
            all_followers_logins = get_all_followers_logins()
            all_following_logins = get_all_following_logins()

            crooks = get_crooks_logins(
                all_followers_logins, all_following_logins)

            unfollow_users(crooks)

        case args if args.list_niceys:
            all_followers_logins = get_all_followers_logins()
            all_following_logins = get_all_following_logins()

            niceys = get_niceys_logins(
                all_followers_logins, all_following_logins)

            print(niceys)

        case args if args.follow_niceys:
            all_followers_logins = get_all_followers_logins()
            all_following_logins = get_all_following_logins()

            niceys = get_niceys_logins(
                all_followers_logins, all_following_logins)

            follow_users(niceys)


if __name__ == "__main__":
    run()
