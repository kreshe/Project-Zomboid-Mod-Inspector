import json
from pathlib import Path


CONFIG_FILE = Path("config.json")


def load_config():

    if not CONFIG_FILE.exists():

        return {}

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(data):

    with open(
        CONFIG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )