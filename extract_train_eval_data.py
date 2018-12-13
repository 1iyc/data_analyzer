#! /usr/bin/env python

import argparse
import os
import random

parser = argparse.ArgumentParser(description="Extract Train & Evaluation Data")

# I&O file
parser.add_argument('--statistic_file', dest="statistic_file", type=str, default="./data/data_statistic.txt",
                    help="Statistic File")

# Data Ratio
parser.add_argument('--eval_ratio', dest="eval_ratio", type=float, default="0.3",
                    help="About How Many Extract Eval Data from Overall Data")

args = parser.parse_args()


def extract_data(statistic_file, eval_ratio):
    dir_path = os.path.dirname(os.path.realpath(statistic_file))

    statistic_list = list(open(statistic_file, 'r', encoding="utf-8").readlines())

    f = open(os.path.join(dir_path, "data_train.txt"), 'w', encoding="utf-8")
    g = open(os.path.join(dir_path, "class_train.txt"), 'w', encoding="utf-8")

    total_count = 0

    single_data = []

    for line in statistic_list:
        line = line.split("\t")
        try:
            data_count = int(line[0])
            data_name = line[1]

            if data_count == 1:
                single_data.append([data_name, line[2]])
            else:
                for class_count, class_name in zip(line[3::3], line[2::3]):
                    for i in range(int(class_count)):
                        g.write(class_name + "\n")
                        f.write(data_name + "\n")

            total_count += data_count

        except ValueError:
            continue

    extra_train_count = len(single_data) - int(total_count * eval_ratio)

    if not extra_train_count > 0:
        print("You Should Lower Eval Ratio")
        print("Adjusted Eval Ratio:", round(len(single_data)/total_count, 2))
        extra_train_count = 0
    else:
        random.shuffle(single_data)

    for i in range(extra_train_count):
        f.write(single_data[0][0] + "\n")
        g.write(single_data[0][1] + "\n")
        del single_data[0]

    f.close()
    g.close()

    f = open(os.path.join(dir_path, "data_eval.txt"), 'w', encoding="utf-8")
    g = open(os.path.join(dir_path, "class_eval.txt"), 'w', encoding="utf-8")

    for data in single_data:
        f.write(data[0] + "\n")
        g.write(data[1] + "\n")

    f.close()
    g.close()


def main():
    extract_data(args.statistic_file, args.eval_ratio)


if __name__ == '__main__':
    main()
