#! /usr/bin/env python

import argparse
import re
import os

parser = argparse.ArgumentParser(description="Pre-processing Data Name")

# I&O file
parser.add_argument('--input_file', dest="input_file", type=str, default="./data/data.txt", help="Data File")
# parser.add_argument('--output_file', dest="output_file", type=str, default="./data/data_cleared.txt",
#                     help="Preprocessed Data Name File")

# Pre-process Mode
parser.add_argument('--DN', dest="DN", type=bool, default=False,
                    help="Replace Dash to None (With Default Function Phase 2.)")
parser.add_argument('--DS', dest="DS", type=bool, default=False,
                    help="Replace Dash to Space (With Default Function Phase 3.)")
parser.add_argument('--SC', dest="SC", type=bool, default=False,
                    help="Delete Single Character\nBe Processed After Default Function Phase 4.")
parser.add_argument('--DC', dest="DC", type=bool, default=False,
                    help="Delete Word with Duplicated Character (cf. XX, MMM)\n\
                            Be Processed After Default Function Phase 4.\n\
                            With SC Option, Processing with SC")
parser.add_argument('--NA', dest="NA", type=str, default=None,
                    help="Delete NA Word in NA File Path\nBe Processed at the Last")

args = parser.parse_args()


def pre_process_data(input_file, dn, ds, sc, dc, na_file):
#    if na_file:
#        with open(na_file, 'r', encoding="utf-8") as e:
#            na_list = [line.rstrip() for line in e]
#    else:

    dir_path = os.path.dirname(os.path.realpath(input_file))
    folder_name = "Pre_Processed" + "_DN"*dn + "_DS"*ds + "_SC"*sc + "_DC"*dc + "_NA"*bool(na_file)
    output_path = os.path.join(dir_path, folder_name)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    g = open(os.path.join(output_path, "data.txt"), 'w', encoding="utf-8")

    if na_file:
        with open(na_file, 'r', encoding="utf-8") as e:
            na_list = [line.rstrip() for line in e]

    with open(input_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            # Phase 1&2.
            if dn and not ds:
                folder_name += "_DN"
                data = re.sub(r'[\.\-]', '', line.strip().upper())
            else:
                data = re.sub(r'[\.]', '', line.strip().upper())

            # Phase 3.
            if ds and not dn:
                folder_name += "_DS"
                data = re.sub(r'[^A-Z]', ' ', data)
            else:
                data = re.sub(r'[^A-Z\-]', ' ', data)

            if not ds and not dn:
                data = ' '.join(x.strip('-') for x in data.split())

            if sc and dc and na_file:
                data = ' '.join(x for x in data.split() if len(x) > 1 and len(set(x)) > 1 and x not in na_list)
            elif sc and dc:
                data = ' '.join(x for x in data.split() if len(x) > 1 and len(set(x)) > 1)
            elif sc and na_file:
                data = ' '.join(x for x in data.split() if len(x) > 1 and x not in na_list)
            elif dc and na_file:
                data = ' '.join(x for x in data.split() if len(set(x)) > 1 and x not in na_list)
            elif sc:
                data = ' '.join(x for x in data.split() if len(x) > 1)
            elif dc:
                data = ' '.join(x for x in data.split() if len(set(x)) > 1)
            elif na_file:
                data = ' '.join(x for x in data.split() if x not in na_list)
            else:
                data = ' '.join(x for x in data.split())

            g.write(data + '\n')


def main():
    if args.DN and args.DS:
        print("Select Either DN or DS")
        exit()
    pre_process_data(args.input_file, args.DN, args.DS, args.SC, args.DC, args.NA)


if __name__ == '__main__':
    main()
