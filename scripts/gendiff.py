import argparse

 
parser = argparse.ArgumentParser(prog='gendiff', description='Generate diff')
parser.add_argument('first_file')
parser.add_argument('second_file')

parser.print_help()