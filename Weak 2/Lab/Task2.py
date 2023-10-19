import numpy as np
s1 = "abcdaf"
s2 = "gbcdf"
rows,cols = (6+1,5+1)
arr = [[0 for i in range(cols)] for j in range(rows)]

def rec(i,j):
    if i>= len(s1):
        return 0;
    if s1[i] != s2[j]:
        arr[i+1][j+1] = 0;
    else:
        arr[i+1][j+1] = 1+ arr[i][j]
    if((j+1)<len(s2)):
        rec(i,j+1)
    else:
        rec(i+1,0)

print('azan')
rec(0,0)
print(max(arr))
print(np.amax(arr))

