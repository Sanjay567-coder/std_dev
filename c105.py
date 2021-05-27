import math
import csv
from stan_dev import stanDev

with open("class1.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0

    for i in data :
        total += int(i)

    mean = total/n
    return mean

sqlist = []

for number in data:
    a = int(number)-mean(data)
    a = a**2
    sqlist.append(a)

sum = 0
for i in sqlist:
    sum = sum + i

result = sum/(len(data)-1)

sta_dev = math.sqrt(result)
print(sta_dev)