from textwrap import indent
from gen_diff.const import SAVED, ADD, REMOVED, TO, FROM, CHILD


SIGN = {
    SAVED: ' ', 
    REMOVED: '-', 
    ADD: '+', 
    CHILD: ' ', 
    FROM: '-', 
    TO: '+'
    }


def sort_diff(i):
    (status, key), value = i
    return key


def to_string(i):
    str_diff = extract_value = ''
    ((status, key), value) = i
    sign = SIGN[status]
    extract_key = key
    if status == CHILD or isinstance(value, dict):
        extract_value = indent(make_format(value, 1), ' ')
    else:
        extract_value = value
    str_diff += '{} {}: {}\n'.format(sign, extract_key, extract_value)
    return str_diff


def make_format(diff, end=0):
    str_diff = ''
    if isinstance(diff, list):
        diff.sort(key=sort_diff)
        for i in diff:
            str_diff += to_string(i)
    else:
        for i in diff:
            str_diff += '   {}: {}\n'.format(i, diff[i])
    str_diff = str_diff.join(['{\n', '}'])
    if end == 0:
        str_diff += '\n'
    return str_diff