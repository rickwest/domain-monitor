import csv


def parse_clc_csv_save_to_database():
    filename = 'raw-firm-data.csv'
    with open(filename, newline='', mode='r') as f:
        # skip the first entry as just headers
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row)


parse_clc_csv_save_to_database()