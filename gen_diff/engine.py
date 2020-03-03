import json
f1 ={"host": "hexlet.io", "timeout": 50, "proxy": "123.234.53.22"}
f2 = {"timeout": 20, "verbose": 'true', "host": "hexlet.io"}
status = {'any': '+', 'removed': '-', 'unchanged': ' '}


def parser(to_file):
    data = json.load(open(to_file))
    return data


def differ(f1, f2):
    x = f1.items()
    y = f2.items()
    result = list()
    for elem in x & y:
        result.extend(make_choice(elem, f1[elem], f2[elem]))
    for elem in x - y:
        result.append(select_removed(elem, f1[elem]))
    for elem in y - x:
        result.append(select_added(elem, f2[elem]))
    return result


def make_choice(elem, f1, f2):
    d = {}
    if f1 == f2:
        d = (assign_status(status['unchanged'], elem, f1))
    elif f1 != f2 and elem not in f2:
       d = (assign_status(status['removed'], elem, f1), assign_status(status[any], elem, f2))
    return d


def select_removed(elem, f1):
    return assign_status(status['removed'], elem, f1)


def select_added(elem, f2):
    return assign_status(status['any'], elem, f2)


def assign_status(status, key, value):
    return (status, key), value


def engine_diff(f1, f2):
    file1 = parser(f1)
    file2 = parser(f2)
    diff = differ(file1, file2)
    diff = json.dumps(diff, indent=2)
    return diff
