import tomllib

VERSION = "0.1.0"

with open("./config.toml", "rb") as config_file:
    config = tomllib.load(config_file)

API_KEY = config["security"]["API_KEY"]
