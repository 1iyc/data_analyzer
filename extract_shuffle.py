#! /usr/bin/env python

import argparse
import random

parser = argparse.ArgumentParser(description="Data Name Clearing")

# I&O file
parser.add_argument('--input_file', dest="input_file", type=str, default="./data/data.txt", help="Data File")
parser.add_argument('--output_file', dest="output_file", type=str, default="./data/data_cleared.txt",
                    help="Cleared Data Name File")

args = parser.parse_args()

def data_shuffle(input_file, output_file):
    g = open(output_file, 'w', encoding="utf-8")
    data_list = list(open(input_file, "r", encoding='utf-8').readlines())

    data_list = random.sample(data_list, len(data_list))

    for i in range(400000):
        g.write(data_list[i])

def main():
    data_shuffle(args.input_file, args.output_file)

if __name__ == '__main__':
    main()

