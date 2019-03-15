#! /usr/bin/env python

import argparse
import name_preprocess
import re


def crawling_data_analyze(data_file, output_file, pre_process, na_file):
    data = dict()
    count = 0
    if pre_process:
        with open(na_file, 'r', encoding="utf-8") as f:
            na_list = [line.strip() for line in f]

    with open(data_file, 'r', encoding="utf-8") as f:
        for line in f:
            try:
                line = line.strip().split("\t")
                line[0] = line[0].strip()
                line[0] = line[0].rstrip(" >>")
                line[0] = re.sub(r"\.\.\.", ' ', line[0])
                if pre_process:
                    line[0] = name_preprocess.pre_process_name(line[0], na_list)
                if line[0] in data:
                    if line[1] in data[line[0]]:
                        data[line[0]][line[1]] += 1
                    else:
                        data[line[0]][line[1]] = 1
                else:
                    data[line[0]] = dict()
                    data[line[0]][line[1]] = 1
                count += 1
                if count % 1000000 == 0:
                    print(count)
            except IndexError:
                print("IndexError: " + line[0])
                continue

    with open(output_file, 'w', encoding="utf-8") as f:
        for i in data:
            record = i + "\t"
            total = 0
            for k in data[i]:
                total += data[i][k]
            for k in sorted(data[i], key=data[i].get, reverse=True):
                record += k + "\t" + str(data[i][k]) + "\t" + str(round(data[i][k] / total * 100, 2)) + "%\t"
            f.write(str(total) + "\t" + record + "\n")


def main():
    parser = argparse.ArgumentParser(description="Crawling Data Analyzer")

    # I&O file
    parser.add_argument('--data_file', dest="data_file", type=str, default="./data/data.txt", help="Crawling Data File")
    parser.add_argument('--output_file', dest="output_file", type=str, default="./data/crawling_statistic_data.txt",
                        help="Output Data File")

    parser.add_argument('--pre_process', dest="pre_process", type=bool, default=False,
                        help="If true, preprocess item name")
    parser.add_argument('--NA', dest="NA", type=str, default="./data/NA.txt",
                        help="Delete NA Word in NA File Path\nBe Processed at the Last")

    args = parser.parse_args()

    crawling_data_analyze(args.data_file, args.output_file, args.pre_process, args.NA)


if __name__ == '__main__':
    main()
