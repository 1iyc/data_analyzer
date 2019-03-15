#! /usr/bin/env python

import re
import argparse


def del_column(data_file, output_file):
    g = open(output_file, 'w', encoding="utf-8")

    with open(data_file, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.strip().split("\t")
            line[1] = re.sub(r'\,', ' ', line[1])
            g.write(line[2] + ", " + line[1] + "\n")


def main():
    parser = argparse.ArgumentParser(description="Crawling Data Analyzer")

    # I&O file
    parser.add_argument('--data_file', dest="data_file", type=str, default="./data/data.txt", help="Crawling Data File")
    parser.add_argument('--output_file', dest="output_file", type=str, default="./data/del_data.txt",
                        help="Output Data File")

    args = parser.parse_args()

    del_column(args.data_file, args.output_file)


if __name__ == '__main__':
    main()
