#! /usr/bin/env python

import argparse
import re

parser = argparse.ArgumentParser(description="Preprocess Data Name")

# I&O file
parser.add_argument('--input_file', dest="input_file", type=str, default="./data/data.txt", help="Data File")
parser.add_argument('--output_file', dest="output_file", type=str, default="./data/data_cleared.txt",
                    help="Preprocessed Data Name File")

parser.add_argument('--na_file', dest="na_file", type=str, default=None, help="Preprocess File with NA Word")

args = parser.parse_args()

def preprocess_data(input_file, output_file, na_file):
    if na_file:
        g = open(output_file + "_na.txt", 'w', encoding="utf-8")
        with open(na_file, 'r', encoding="utf-8") as e:
            na_list = [line.rstrip() for line in e]
    else:
        g = open(output_file, 'w', encoding="utf-8")

    with open(input_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            data = re.sub(r'[\.]', '', line.strip().upper())
            data = re.sub(r'[^A-Z]', ' ', data)
            if na_file:
                data = ' '.join(x for x in data.split() if x not in na_list and len(x) > 1)
                g.write(data + '\n')
            else:
                data = ' '.join(x for x in data.split() and len(x) > 1)
                g.write(data + '\n')


def main():
    preprocess_data(args.input_file, args.output_file, args.na_file)

if __name__ == '__main__':
    main()

