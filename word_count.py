#! /usr/bin/env python

import argparse
import re

parser = argparse.ArgumentParser(description="Count Words in Data")

# input file
parser.add_argument('--data_file', dest="data_file", type=str, default="./data/data.txt", help="Data File Path")

args = parser.parse_args()

def count_words(data_file):
    data_list = list(open(data_file, 'r', encoding="utf-8").readlines())

    words = dict()
    total_data_count = len(data_list)
    count = 0

    for data in data_list:
        data = data.split()
        for word in data:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        count += 1
        if count % int(total_data_count * 0.01) == 0:
            print(str(int(count/total_data_count*100)) + "%....")

    with open(data_file + "_wordcount.txt", 'w', encoding="utf-8") as f:
        for k in sorted(words, key=words.get, reverse=True):
            f.write(k + "\t" + str(words[k]) + "\n")


def main():
    count_words(args.data_file)


if __name__ == '__main__':
    main()

