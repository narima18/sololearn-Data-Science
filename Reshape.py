import numpy as np
r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)
c=len(arr)/r  
new_arr=arr.reshape(int(r),int(c))
print(new_arr.round(2))
