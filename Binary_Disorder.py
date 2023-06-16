y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]

import numpy as np
y_true = np.array(y_true)
y_pred= np.array(y_pred)

tp=sum(y_true & y_pred)
fp=sum(~y_true &  y_pred)
fn=sum(y_true & ~y_pred)
tn=len(y_true)-tp-fp-fn

print(np.array([[tp,fp],[fn,tn]],dtype='f'))
