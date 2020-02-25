import json


def parser(file):
    data = json.load(open(file))
    return data


def differ():

def engine_diff(f1, f2):
    file1 = parser(f1)
    file2 = parser(f2)
    diff = differ(file1, file2)
    return diff