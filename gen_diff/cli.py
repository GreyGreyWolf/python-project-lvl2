import argparse
from gen_diff import format


def formatter(name):
    if name == format.JSON:
        return format.json
    elif name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    raise argparse.ArgumentTypeError(
        'Unknown formatter: "{}". Use one of this: {}'.format(
            name,
            ', '.join(format.FORMATTERS),
        )
    )


def init_argparser():
    parser = argparse.ArgumentParser(
        prog='gendiff', description='Generate difference between two files')
    parser.add_argument('first_file', help='first file name')
    parser.add_argument('second_file', help='second file name')
    parser.add_argument(
        '-f', '--format',
        default=format.DEFAULT,
        help='set format of output: "plain", "json", "default"',
        type=formatter,
    )
    return parser
