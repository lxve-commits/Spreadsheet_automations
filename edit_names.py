import csv

# your csv filename
filename = 'names.csv'

# resultant filename
res_filename = 'new_names.csv'

# open a file for reading
with open(filename, 'r') as csvfile:
    # create a csv reader object
    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    next(csvreader)

    data = []
    for row in csvreader:
        for i in range(int(row[1])):
            data.append([row[0], '18-25'])
        for i in range(int(row[2])):
            data.append([row[0], '26-35'])

# writing to csv file
with open(res_filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the headers
    csvwriter.writerow(['Name', 'Age'])

    # writing the data rows
    csvwriter.writerows(data)