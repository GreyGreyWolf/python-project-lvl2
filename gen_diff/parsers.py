import json
import os.path
import yaml


def parser(to_file):
    root, name_file = os.path.split(to_file)
    first_name, format = os.path.splitext(name_file)
    if format == '.json':
        data = json.load(open(to_file))
    elif format == '.yml':
        data = yaml.safe_load(open(to_file))
    else:
        with open(to_file, 'r') as input_file:
            data = input_file.read()
    return data
