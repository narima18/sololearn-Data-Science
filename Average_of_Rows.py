import numpy as np
n, p = [int(x) for x in input().split()]
list = []

for i in range (n):
    list.append([float(j) for j in input().split()])
    
arr = np.array(list)
mean = arr.mean(axis = 1).round(2)
print (mean)
