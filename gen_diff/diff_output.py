import argparse
from gen_diff import engine
from gen_diff.formatters import to_str, to_text, to_json


def turn(arg):
    if arg == 'plain':
        return to_text.make_format
    elif arg == 'json':
        return to_json.make_format
    else:
        return to_str.make_format


parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
      '-f', '--format', choices=['plain', 'json'],
      default=0, help='set format of output')
args = parser.parse_args()
diff = engine.engine_diff(
    args.first_file,
    args.second_file,
    turn(args.format)
    )
print(diff)
