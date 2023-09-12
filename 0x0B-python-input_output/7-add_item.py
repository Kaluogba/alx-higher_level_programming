#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
import json
from sys import argv
from os.path import exists


def load_items():
    if exists("add_item.json"):
        with open("add_item.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        return []


def save_items(items):
    with open("add_item.json", "w") as file:
        json.dump(items, file)


arguments = argv[1:]
existing_items = load_items()
existing_items.extend(arguments)
save_items(existing_items)
