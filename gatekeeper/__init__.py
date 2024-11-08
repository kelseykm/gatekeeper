import tomllib
from pathlib import Path
import os.path

VERSION = "0.1.0"

current_file_path = Path(__file__)
config_file_path = os.path.join(current_file_path.parent.parent, "config.toml")

with open(config_file_path, "rb") as config_file:
    config = tomllib.load(config_file)

    API_KEY = config["security"]["API_KEY"]
