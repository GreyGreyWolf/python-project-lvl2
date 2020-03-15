from gen_diff.parsers import parser
from gen_diff.const import SAVED, ADD, REMOVED, TO, FROM, CHILD


def is_children(f1, f2):
    return isinstance(f1, dict) and isinstance(f2, dict) and f1 != f2


def differ(f1, f2):
    x = f1.keys()
    y = f2.keys()
    result = list()
    for elem in x & y:
        result.extend(make_choice(elem, f1[elem], f2[elem]))
    for elem in x - y:
        result.append(select_removed(elem, f1[elem]))
    for elem in y - x:
        result.append(select_added(elem, f2[elem]))
    return result


def make_choice(elem, f1, f2):
    new_dict = {}
    if f1 == f2:
        new_dict = (assign_status(SAVED, elem, f1), )
    elif is_children(f1, f2):
        new_dict = (assign_status(CHILD, elem, differ(f1, f2)), )
    elif not is_children(f1, f2):
        new_dict = (assign_status(FROM, elem, f1),
                    assign_status(TO, elem, f2))
    return new_dict


def select_removed(elem, f1):
    return assign_status(REMOVED, elem, f1)


def select_added(elem, f2):
    return assign_status(ADD, elem, f2)


def assign_status(status, key, value):
    return (status, key), value


def engine_diff(f1, f2, vizual):
    file1 = parser(f1)
    file2 = parser(f2)
    diff = vizual(differ(file1, file2))
    return diff
