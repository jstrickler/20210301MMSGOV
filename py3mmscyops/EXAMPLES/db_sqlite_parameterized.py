#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/presidents.db") as s3conn:
    s3cursor = s3conn.cursor()

    party_query = '''
    select firstname, lastname
    from presidents
        where party = :party_name
    '''  # <1>

    for party_name in 'Federalist', 'Whig':
        print(party_name)
        s3cursor.execute(party_query, {'party_name': party_name})  # <2>
        print(s3cursor.fetchall())
        print()

    s3cursor.execute('select * from presidents where 1 = 2')
    for column in s3cursor.description:
        print(column)
    column_names = [d[0] for d in s3cursor.description]
    print(column_names)
    print("-" * 60)

    s3cursor.execute("select name from sqlite_master where type='table'")
    for row in s3cursor.fetchall():
        print(row)

