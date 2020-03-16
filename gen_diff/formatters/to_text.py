from gen_diff.engine import assign_status
from gen_diff.formatters.to_str import sort_diff
from gen_diff.const import SAVED, ADD, REMOVED, TO, FROM, CHILD


def to_string(i):
    adj = ''
    (status, key), value = i
    if status == REMOVED:
        adj = '.\n'
    elif status == FROM:
        adj = ". From '{}' to ".format(value)
    elif status == TO:
        string = "'{}'.\n".format(value)
        return string
    elif status == ADD:
        adj = " with value: '{}'.\n".format(value)
    string2 = "Property '{}' was {}{}".format(key, status, adj)
    return string2


def select(i):
    (status, key), value = i
    if status == ADD and type(value) is dict:
        i = assign_status(status, key, 'complex value')
    elif status == SAVED:
        return ''
    return to_string(i)


def make_format(diff):
    str_diff = ''
    diff.sort(key=sort_diff)
    for i in diff:
        (status, key), value = i
        if status == CHILD:
            str_diff += make_format(deepen(key, value))
        else:
            str_diff += select(i)
    return str_diff


def deepen(key, value):
    new_diff = list()
    for i in value:
        (status_v, key_v), value_v = i
        new_key = ".".join([key, key_v])
        new_diff.append(assign_status(status_v, new_key, value_v))
    return new_diff
