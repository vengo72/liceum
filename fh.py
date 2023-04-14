import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--file", action='store_true')
parser.add_argument("arg", type=str, nargs='*')
args = parser.parse_args()

with open(args.arg[0]) as file:
    f = file.readlines()
    d = dict()
    for i in f:
        t = i[:-1].split(':')
        if t[2] == args.type:
            d[t[1]] = round(int(t[4]) / int(t[3]), 1)
    with open('relation.json', 'w') as file1:
        json.dump(d, file1)




