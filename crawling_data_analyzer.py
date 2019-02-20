#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Crawling Data Analyzer")

# I&O file
parser.add_argument('--data_file', dest="data_file", type=str, default="./data/data.txt", help="Crawling Data File")
parser.add_argument('--output_file', dest="output_file", type=str, default="./data/crawling_statistic_data.txt",
                    help="Output Data File")

args = parser.parse_args()


def crawling_data_analyze(data_file, output_file):
    data = dict()
    count = 0

    with open(data_file, 'r', encoding="utf-8") as f:
        for line in f:
            try:
                line = line.strip().split("\t")
                line[0] = line[0].strip()
                line[0] = line[0].rstrip(" >>")
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
    crawling_data_analyze(args.data_file, args.output_file)


if __name__ == '__main__':
    main()
