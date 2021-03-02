import os

FOLDER = "DATA"
FILE_NAME = "mary.txt"

file_path = os.path.join(FOLDER, FILE_NAME)

file_in = open(file_path)

file_in.close()

# file modes
# r w a x   TEXT  r is default
# rb wb ab xb   BINARY
with open(file_path) as file_in:
    for raw_line in file_in:
        line = raw_line.rstrip()
        print(line)
print("-" * 60)

with open(file_path) as file_in:
    contents = file_in.read()  # read whole file
    print("normal:")
    print(contents)
    print("raw:")
    print(repr(contents))
print("-" * 60)

with open(file_path) as file_in:
    all_lines = file_in.readlines()
    print(all_lines)
print("-" * 60)

with open(file_path) as file_in:
    all_lines_without_nl = file_in.read().splitlines()
    print(all_lines_without_nl)