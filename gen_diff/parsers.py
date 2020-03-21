import json
import yaml


def parser(file_path):
    format = file_path[file_path.rfind('.'):]
    if format == '.json':
        data = json.load(open(file_path))
    elif format == '.yml':
        data = yaml.safe_load(open(file_path))
    return data
