import csv

def read_csv(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_row = {}
            for col, val in row.iteritems():
                if val.strip() != '':
                    data_row[col] = try_int(val)
            data.append(data_row)

    return data

def try_int(val):
    try:
        s = int(val)
        return s
    except ValueError:
        return val
