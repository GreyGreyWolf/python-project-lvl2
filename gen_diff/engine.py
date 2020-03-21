from gen_diff import parsers
from gen_diff.const import SAVED, ADD, REMOVED, TO, FROM, CHILD
from gen_diff.cli import init_argparser


def gendiff():
    parser = init_argparser()
    args = parser.parse_args()
    diff = get_diff(args.first_file, args.second_file)
    print(args.format(diff))


def finding_difference(file1, file2):
    x = file1.keys()
    y = file2.keys()
    result = list()
    for elem in x & y:
        result.extend(make_choice(elem, file1[elem], file2[elem]))
    for elem in x - y:
        result.append(make_pair(REMOVED, elem, file1[elem]))
    for elem in y - x:
        result.append(make_pair(ADD, elem, file2[elem]))
    return result


def make_choice(elem, file1, file2):
    new_dict = {}
    if file1 == file2:
        new_dict = (make_pair(SAVED, elem, file1), )
    elif (isinstance(file1, dict) and isinstance(
         file2, dict) and file1 != file2):
        new_dict = (make_pair(CHILD, elem, finding_difference(file1, file2)), )
    elif not (isinstance(file1, dict) and isinstance(
         file2, dict) and file1 != file2):
        new_dict = (make_pair(FROM, elem, file1),
                    make_pair(TO, elem, file2))
    return new_dict


def make_pair(status, key, value):
    return (status, key), value


def get_diff(file1, file2):
    parsed_file1 = parsers.parser(file1)
    parsed_file2 = parsers.parser(file2)
    diff = finding_difference(parsed_file1, parsed_file2)
    return diff
