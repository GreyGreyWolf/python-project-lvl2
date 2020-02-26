import argparse
from gen_diff import engine

parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()
print(engine.engine_diff(args.first_file, args.second_file))
