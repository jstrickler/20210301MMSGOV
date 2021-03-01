from argparse import ArgumentParser

parser = ArgumentParser(description="Faux grep")
parser.add_argument("-i", dest="ignore_case", action="store_true", help="ignore case")
parser.add_argument("-f", dest="show_file_name", action="store_true", help="show file name")
parser.add_argument("search_term", help="search term")
parser.add_argument("files", nargs="+", help="files to saerch")

args = parser.parse_args()

if args.ignore_case:
    args.search_term = args.search_term.lower()

for file_name in args.files:
    with open(file_name) as file_in:
        for raw_line in file_in:
            orig_line = raw_line.rstrip()
            if args.ignore_case:
                raw_line = raw_line.lower()
            if args.search_term in raw_line:
                if args.show_file_name:
                    print(file_name, end=' ')
                print(orig_line)
