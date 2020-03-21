from gen_diff import engine
from gen_diff.format.default import sort_diff
from gen_diff.const import SAVED, ADD, REMOVED, TO, FROM, CHILD


def to_string(data):
    string1 = ''
    (status, key), value = data
    if status == REMOVED:
        string1 = '.\n'
    elif status == FROM:
        string1 = ". From '{}' to ".format(value)
    elif status == TO:
        string = "'{}'.\n".format(value)
        return string
    elif status == ADD:
        string1 = " with value: '{}'.\n".format(value)
    string2 = "Property '{}' was {}{}".format(key, status, string1)
    return string2


def select(data):
    (status, key), value = data
    if status == ADD and type(value) is dict:
        data = engine.make_pair(status, key, 'complex value')
    elif status == SAVED:
        return ''
    return to_string(data)


def format(diff):
    str_diff = ''
    diff.sort(key=sort_diff)
    for elem in diff:
        (status, key), value = elem
        if status == CHILD:
            str_diff += format(deepen(key, value))
        else:
            str_diff += select(elem)
    return str_diff


def deepen(key, value):
    new_diff = list()
    for elem in value:
        (status_v, key_v), value_v = elem
        new_key = ".".join([key, key_v])
        new_diff.append(engine.make_pair(status_v, new_key, value_v))
    return new_diff
