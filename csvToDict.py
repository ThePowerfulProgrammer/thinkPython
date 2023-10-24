import csv

def read_csv_to_dict(filename):
    directory = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:
            lastName, firstName, number = row
            directory[(lastName, firstName)] = number
    return directory

filename = 'personInfo.csv'  # Update with your CSV filename
directory = read_csv_to_dict(filename)

# here our key is a tuple, therefore directory[(last,first)] = value
for last,first in directory:
    print(last, " ", first," ", directory[(last,first)])