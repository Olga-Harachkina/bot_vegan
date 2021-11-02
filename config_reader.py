import json
import pprint


# уаау
def read_json(path="meny.json"):
# def read_json():

    with open("meny.json", "r", encoding='utf-8') as read_file:
        menu = json.load(read_file)

    pprint.pprint(menu.keys())
def