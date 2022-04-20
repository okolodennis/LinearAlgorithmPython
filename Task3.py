import csv

with open("datapoints.csv", newline='') as file_name:
 readData = csv.reader(file_name)
 listData = list(readData)
 listData.pop(0)
 
 a = 10
 b = 0
 
 for row in listData:
     x = float(row[0])
     y = a * x + b
     print("y = " + str(y))
  




