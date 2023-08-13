from pathlib import Path
import json
import csv

with open('C:/Users/Dell/Desktop/movies.json') as jsonObj:
    data = json.load(jsonObj)
    with open("C:/Users/Dell/Desktop/python.csv",'w') as file:
        writer = csv.writer(file)
        writer.writerow(['id','title','year'])
        for items in data:
            writer.writerow([items['id'],items['title'],items['year']])
    
# solve the rows problem!!!