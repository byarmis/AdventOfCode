import csv

def night_1():
    with open('5784/noahs-customers.csv') as f:
        reader = csv.DictReader(f)
        lines = [line for line in reader]

    letters_to_num = {
            'a':2,
            'b':2,
            'c':2,

            'd':3,
            'e':3,
            'f':3,

            'g':4,
            'h':4,
            'i':4,

            'j':5,
            'k':5,
            'l':5,

            'm':6,
            'n':6,
            'o':6,

            'p':7,
            'q':7,
            'r':7,
            's':7,

            't':8,
            'u':8,
            'v':8,

            'w':9,
            'x':9,
            'y':9,
            'z':9,
            }

    for line in lines:
        if '0' in line['phone']:
            continue

        name_as_number = ''.join(str(letters_to_num.get(l.lower(), '')) for l in line['name'].split()[1] if l)
        number_cleaned = ''.join(l for l in line['phone'] if l.isdigit())

        if name_as_number == number_cleaned:
            return line['phone']

print('Night 1: ', night_1())

