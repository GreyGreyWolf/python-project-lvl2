from textwrap import indent
from gen_diff.engine import SAVED, ADD, REMOVED, TO, FROM, CHILD


SIGN = {
    SAVED: ' ',
    REMOVED: '-',
    ADD: '+',
    CHILD: ' ',
    FROM: '-',
    TO: '+'
    }


def sort_diff(data):
    (status, key), value = data
    return key


def to_string(data):
    str_diff = string_value = ''
    ((status, key), value) = data
    sign = SIGN[status]
    string_key = key
    if status == CHILD or isinstance(value, dict):
        string_value = indent(format(value, 1), ' ')
    else:
        string_value = value
    str_diff += '{} {}: {}\n'.format(sign, string_key, string_value)
    return str_diff


def format(diff, end=0):
    str_diff = ''
    if isinstance(diff, list):
        diff.sort(key=sort_diff)
        for elem in diff:
            str_diff += to_string(elem)
    else:
        for elem in diff:
            str_diff += '   {}: {}\n'.format(elem, diff[elem])
    str_diff = str_diff.join(['{\n', '}'])
    if end == 0:
        str_diff += '\n'
    return str_diff
