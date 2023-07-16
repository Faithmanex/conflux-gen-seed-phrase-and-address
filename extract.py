import csv

csv_file = 'test.csv'
output_file = 'addresses.txt'

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    addresses = [line[-1].strip().split()[-1] for line in csv_reader]

with open(output_file, 'w') as file:
    file.write('\n'.join(addresses))
