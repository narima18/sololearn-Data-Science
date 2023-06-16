import math
import numpy as np
n = int(input())
ce1=[0,0] 
ce2=[2,2] 
cl1=np.empty([0,2], float)
cl2=np.empty([0,2], float)

for i in range(n):
    x = [float(j) for j in input().split()]
    d21 = (np.array(ce1)-np.array(x))**2
    d1=math.sqrt(d21.sum())
    d2 = math.sqrt(((np.array(ce2)-np.array(x))**2).sum()) 
    if d1<=d2:
       cl1 = np.append(cl1, np.array([x]), axis=0) 
    else: 
       cl2 = np.append(cl2, np.array([x]), axis=0)  
if cl1.shape[0]!=0:
   print(np.mean(cl1,axis=0).round(2))
else:
   print(None)
if cl2.shape[0]!=0:
   print(np.mean(cl2,axis=0).round(2))
else:
   print(None)
