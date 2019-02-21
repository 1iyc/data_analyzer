#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Make train data by crawled statistic data")

# I&O file
parser.add_argument('--input_file', dest="input_file", type=str, default="./data/crawling_statistic_data.txt",
                    help="Statistic data file path")
parser.add_argument('--output_file', dest="output_file", type=str, default="./data/train_data.txt",
                    help="Output data file path")

args = parser.parse_args()


def statistic_to_train_data(input_file, output_file):
    g = open(output_file, 'w', encoding="utf-8")

    with open(input_file, 'r', encoding="utf-8") as f:
        for line in f:
            line = line.split('\t')
            if len(line[2]) >= 6:
                line[2] = line[2][0:6]
            else:
                if len(line) >= 6:
                    if len(line[5]) >= 6:
                        line[2] = line[5][0:6]
                    else:
                        continue
                else:
                    continue
            g.write(line[0] + "\t" + line[1] + "\t" + line[2] + "\n")


def main():
    statistic_to_train_data(args.input_file, args.output_file)


if __name__ == '__main__':
    main()
