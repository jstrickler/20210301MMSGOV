import csv

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

with open('people.txt', 'w') as people_out:
    for person in people:
        record = '\t'.join(person)
        people_out.write(record + '\n')

with open('people.csv', 'w') as people_out:
    wtr = csv.writer(people_out)
    for person in people:
        wtr.writerow(person)

with open('people.txt') as people_in:
    with open('old_nerds.txt', "w") as old_out:
        with open('young_nerds.txt', "w") as young_out:
            for raw_line in people_in:
                fields = raw_line.rstrip().split('\t')
                if fields[-1] >= '1970-01-01':
                    young_out.write(raw_line)
                else:
                    old_out.write(raw_line)
