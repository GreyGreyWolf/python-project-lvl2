import json


status = {'added or change': ' + ', 'removed': ' - ', 'not chenged': '   '}


def parser(to_file):
    data = json.load(open(to_file))
    return data


def differ(f1, f2):
    new_dict = {}
    for key, value in f1.items():
        if key in f2 and f1[key] == f2[key]:
            new_dict.update(
                {status['not chenged'] + key: f1[key]})  # Not changed
        elif key not in f2:
            new_dict.update({status['removed'] + key: f1[key]})  # Removed
        elif key in f2 and f1[key] != f2[key]:
            new_dict.update({status['removed'] + key: f1[key]})
            new_dict.update(
                {status['added or change'] + key: f2[key]})  # Changed
    for key, value in f2.items():
        if key not in f1:
            new_dict.update(
                {status['added or change'] + key: f2[key]})  # Added
    return new_dict


def engine_diff(f1, f2):
    file1 = parser(f1)
    file2 = parser(f2)
    diff = differ(file1, file2)
    diff = json.dumps(diff, indent=2)
    return diff.replace('\"', '')
