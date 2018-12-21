#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Refining Data & Class File before clustering")

# I&O file
parser.add_argument('--input_file', dest="input_file", type=str, default="./data/input.xls",
                    help="Excel Data File Path")
parser.add_argument('--output_data', dest="output_data", type=str, default="./data/data.txt",
                    help="Output Data File Path")
parser.add_argument('--output_class', dest="output_class", type=str, default="./data/class.txt",
                    help="Output Class File Path")

parser.add_argument('--one_output', dest="one_output", type=str, default=None,
                    help="Get a File Data with Class")

args = parser.parse_args()


def split_data_class(input_file, output_data, output_class, one_output):
    g = open(output_data, 'w', encoding="utf-8")
    h = open(output_class, 'w', encoding="utf-8")
    if one_output:
        e = open(one_output, 'w', encoding="utf-8")

    with open(input_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            data = line.split('\t')
            g.write(''.join(data[:-1]) + '\n')
            h.write(data[-1].strip() + '\n')
            if one_output:
                e.write(''.join.data[:-1] + "\t" + data[-1].strip() + '\n')


def main():
    split_data_class(args.input_file, args.output_data, args.output_class, args.one_output)


if __name__ == '__main__':
    main()

