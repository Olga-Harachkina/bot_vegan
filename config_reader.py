import json


def read_json(path="meny.json"):
    with open(path, "r", encoding='utf-8') as read_file:
        return json.load(read_file)
