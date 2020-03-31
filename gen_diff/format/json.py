import json


def format(diff):
    return json.dumps(diff, indent=4)
