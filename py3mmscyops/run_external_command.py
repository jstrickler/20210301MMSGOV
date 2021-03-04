from subprocess import run, PIPE, CalledProcessError
from glob import glob
import shlex

file_arg = "../DATA/*.csv"
files = glob(file_arg)

raw_cmd = "netstat -an"

cmd_words = shlex.split(raw_cmd) # + files

try:
    proc = run(cmd_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err)
else:
    output = proc.stdout.decode()
    output_lines = output.splitlines()
    for line in output_lines:
        if 'ESTAB' in line:
            line = line.rstrip()
            print(line)
