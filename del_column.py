import re

g = open("C:/data/pcs_data/crawling/data.csv", 'w', encoding="utf-8")

with open("C:/data/pcs_data/crawling/train_data_0220.txt", 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip().split("\t")
        line[1] = re.sub(r'\,', ' ', line[1])
        g.write(line[2] + ", " + line[1] + "\n")
