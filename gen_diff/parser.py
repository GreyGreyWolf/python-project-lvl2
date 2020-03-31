import os
import json
import yaml


def get_path(path):
    path = os.path.expanduser(path)
    path = os.path.abspath(os.path.normpath(path))
    return path


def get_data_from(file):
    path = get_path(file)
    _, ext = os.path.splitext(file)
    if ext in {'.json', 'jsn'}:
        data = json.load(open(path))
    elif ext in {'.yml', '.yaml'}:
        data = yaml.safe_load(open(path))
    return data
