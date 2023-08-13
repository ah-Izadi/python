import csv
with open("C:/Users/Dell/Desktop/python.csv",'w') as file:
    writer = csv.writer(file)
    writer.writerow(['product id','height','price'])
    writer.writerow([100,2,15])
    writer.writerow([129,1.5,12])