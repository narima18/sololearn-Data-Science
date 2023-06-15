import numpy as np
n, p = [int(x) for x in input().split()]
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])

y = [float(x) for x in input().split()]

x1 = np.array(X)
y1 = np.array(y)

X_T = x1.T
XTX = np.dot(X_T, X)

XTX_INV = np.linalg.inv(XTX)

XTXINVXT = np.dot(XTX_INV, X_T)
beta = np.dot(XTXINVXT, y)
print(beta.round(2))
