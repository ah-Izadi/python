import csv
with open("C:/Users/Dell/Desktop/python.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        print(row)