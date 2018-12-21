#! /usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Data Name Clearing")

# I&O file
parser.add_argument('--data_file', dest="data_file", type=str, default="./data/data.txt", help="Data File")
parser.add_argument('--class_file', dest="class_file", type=str, default="./data/class.txt",
                    help="Class File")
parser.add_argument('--output_file', dest="output_file", type=str, default="./data/data_static.txt", help="Output File")

args = parser.parse_args()


def data_verify(data_file, class_file, output_file):
    data_list = list(open(data_file, 'r', encoding="utf-8").readlines())
    class_list = list(open(class_file, 'r', encoding="utf-8").readlines())

    data = dict()
    total_data_count = len(data_list)
    count = 0

    print("Dictionary Making...")
    for i in range(len(data_list)):
        data_line = data_list[i].strip()
        class_line = class_list[i].strip()
        if data_line in data:
            if class_line in data[data_line]:
                data[data_line][class_line] += 1
            else:
                data[data_line][class_line] = 1
        else:
            data[data_line] = dict()
            data[data_line][class_line] = 1
        count += 1
        if count % int(total_data_count * 0.01) == 0:
            print(str(int(count/total_data_count*100)) + "%....")

    print("Static File Writing...")
    with open(output_file, 'w', encoding="utf-8") as f:
        for i in data:
            record = i + "\t"
            # f.write(i + "\t")
            total = 0
            for k in data[i]:
                total += data[i][k]
            for k in sorted(data[i], key=data[i].get, reverse=True):
                # f.write(k + "\t" + str(data[i][k]) + "\t" + str(round(data[i][k]/total*100, 2)) + "%\t")
                record += k + "\t" + str(data[i][k]) + "\t" + str(round(data[i][k]/total*100, 2)) + "%\t"
            f.write(str(total) + "\t" + record + "\n")


def main():
    data_verify(args.data_file, args.class_file, args.output_file)


if __name__ == '__main__':
    main()
