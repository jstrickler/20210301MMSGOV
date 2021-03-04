#!/usr/bin/env python

import sys
import os
from datetime import datetime

if len(sys.argv) < 2:
    start_dir = "."
else:
    start_dir = sys.argv[1]

for base_name in sorted(os.listdir(start_dir)):  # <1>
    file_name = os.path.join(start_dir, base_name)
    if os.access(file_name, os.W_OK | os.R_OK | os.X_OK):  # <2>
        print(file_name, "is writable")

for base_name in sorted(os.listdir(start_dir)):  # <1>
    file_name = os.path.join(start_dir, base_name)
    s = os.stat(file_name)
    print(file_name, s)
    print("size:", os.path.getsize(file_name))
    raw_ts = os.path.getmtime(file_name)
    timestamp = datetime.fromtimestamp(raw_ts)
    print("timestamp:", timestamp)
    print()