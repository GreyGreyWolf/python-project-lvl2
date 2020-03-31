from gen_diff import parser
from gen_diff.cli import init_argparser


SAVED = 'no change'
REMOVED = 'removed'
ADD = 'added'
CHILD = 'child'
FROM = 'changed'
TO = 'to'


def gendiff():
    parser = init_argparser()
    args = parser.parse_args()
    diff = get_diff(args.first_file, args.second_file)
    print(args.format(diff))


def difference(file1, file2):
    x = file1.keys()
    y = file2.keys()
    result = list()
    for elem in x & y:
        result.extend(compare_childs(elem, file1[elem], file2[elem]))
    for elem in x - y:
        result.append(make_pair(REMOVED, elem, file1[elem]))
    for elem in y - x:
        result.append(make_pair(ADD, elem, file2[elem]))
    return result


def compare_childs(elem, file1, file2):
    new_tuple = {}
    if file1 == file2:
        elem = (make_pair(SAVED, elem, file1), )
    elif (isinstance(file1, dict) and isinstance(
         file2, dict) and file1 != file2):
        new_tuple = (make_pair(CHILD, elem, difference(file1, file2)), )
    elif not (isinstance(file1, dict) and isinstance(
         file2, dict) and file1 != file2):
        new_tuple = (make_pair(FROM, elem, file1),
                    make_pair(TO, elem, file2))
    return new_tuple


def make_pair(status, key, value):
    return (status, key), value


def get_diff(file1, file2):
    parsed_file1 = parser.parser(file1)
    parsed_file2 = parser.parser(file2)
    diff = difference(parsed_file1, parsed_file2)
    return diff
