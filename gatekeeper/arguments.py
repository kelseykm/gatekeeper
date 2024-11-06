import argparse
from . import VERSION


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gatekeeper", description="Manage followers and following users on Github")
    parser.add_argument("-v", "--version", action="version",
                        version=f"%(prog)s {VERSION}")

    flags = parser.add_mutually_exclusive_group(required=True)

    flags.add_argument("--list_followers",
                       action="store_true", help="List all your followers")
    flags.add_argument("--list_following", action="store_true",
                       help="List all users you're following")
    flags.add_argument("--list_crooks", action="store_true",
                       help="List all users you're following but aren't following you back")
    flags.add_argument("--unfollow_crooks", action="store_true",
                       help="Unfollow all users who aren't following you back")
    flags.add_argument("--list_niceys", action="store_true",
                       help="List all users that are following you but you aren't following them back")
    flags.add_argument("--follow_niceys", action="store_true",
                       help="Follow all users that you are following you but you aren't following them")

    return parser


def main() -> argparse.Namespace:
    parser = create_parser()
    args = parser.parse_args()

    return args
