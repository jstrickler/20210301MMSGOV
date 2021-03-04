import os
file_names = 'wombats.txt', 'mary.txt', 'betty.txt', 'glock.blizx', 'alice.txt'

for file_name in file_names:
    file_path = os.path.join('DATA', file_name)
    print(file_name, end=' ')
    try:
        with open(file_path) as wombats_in:
            pass
    except FileNotFoundError as err:
        print(err)
    else:
        print("Opened OK")
print("-" * 60)

colors = ['red', 'blue', 'purple', 'orange']
try:
    print(colors[8])
except (IndexError, TypeError) as err:
    print(err)
except KeyError as err:
    print("HUH:", err)
except Exception as err:
    print(err)

import sqlite3

try:
    conn = sqlite3.connect('foo.db')
except sqlite3.OperationalError as err:
    print(err)
    exit(1)
else:
    pass  # do your DB thang here
finally:
    if conn:
        conn.close()




