import json


def parser(to_file):
    data = json.load(open(to_file))
    return data
