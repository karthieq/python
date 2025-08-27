import csv

with open('sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('sample_mod.csv', 'w', newline='\n') as csv_new_file:
        fieldnames = ['first','last','email']
        csv_writer = csv.DictWriter(csv_new_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
