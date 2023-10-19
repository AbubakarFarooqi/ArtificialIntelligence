s1 = "arts"
s2 = "maths"

rows,cols = (4+1,5+1)
arr = [[0 for i in range(cols)] for j in range(rows)]
x = 0
for i in range(rows):
    arr[i][0] = x
    x+=1
x = 0
for i in range(cols):
    arr[0][i] = x
    x+=1

def editDistance(i,j):
    if(i >=len(s1) or j>=len(s2)):
        return
    if(s1[i] == s2[j]):
        arr[i+1][j+1] = min(arr[i][j+1]+1 , arr[i+1][j]+1,arr[i][j])
    else:
        arr[i+1][j+1] = min(arr[i][j+1]+1 , arr[i+1][j]+1,arr[i][j]+1)
    if((j+1)<len(s2)):
        editDistance(i,j+1)
    else:
        editDistance(i+1,0)
editDistance(0,0)
print(arr)
print(arr[4][5])

    

