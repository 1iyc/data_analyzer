#! /usr/bin/env python

import argparse
import re

parser = argparse.ArgumentParser(description="Data Name Clearing")

# I&O file
parser.add_argument('--input_file', dest="input_file", type=str, default="./data/data.txt", help="Data File")
parser.add_argument('--output_file', dest="output_file", type=str, default="./data/data_cleared.txt",
                    help="Cleared Data Name File")

parser.add_argument('--na_file', dest="na_file", type=str, default=None, help="Cleared File with NA Word")

args = parser.parse_args()

def clear_data(input_file, output_file, na_file):
    g = open(output_file, 'w', encoding="utf-8")
    if na_file:
        h = open(output_file + "_na_cleared.txt", 'w', encoding="utf-8")
        with open(na_file, 'r', encoding="utf-8") as e:
            na_list = [line.rstrip() for line in e]

    with open(input_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            data = re.sub(r'[^ABCDEFGHIJKLMNOPQRSTUVWXYZ-]', ' ', line.strip().upper())
            data = ' '.join(x.strip('-') for x in data.split())
            data = ' '.join(x for x in data.split() if len(x) > 1 and len(set(x)) > 1)

            g.write(data + '\n')

            if na_file:
                data = ' '.join(x for x in data.split() if x not in na_list)
                h.write(data + '\n')


def main():
    clear_data(args.input_file, args.output_file, args.na_file)

if __name__ == '__main__':
    main()

