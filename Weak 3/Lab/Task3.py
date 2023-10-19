s1 = "AGT"
s2 = "AAGC"
rows,cols = (3+1,4+1)
arr = [[0 for i in range(cols)] for j in range(rows)]
dict = {}
x = 0
for i in range(rows):
    arr[i][0] = x
    x-=2
x = 0
for i in range(cols):
    arr[0][i] = x
    x-=2

def rec(i,j):
    if(i >=len(s1) or j>=len(s2)):
        return
    if(s1[i] == s2[j]):
        upp = arr[i+1-1][j+1]-2
        left = arr[i+1][j+1-1]-2
        diag = arr[i+1-1][j+1-1]+1
        maxi = max(upp,left,diag)
        if maxi == upp:
            dict[str(i+1)+","+str(j+1)] = "upp"
        elif maxi == left:
            dict[str(i+1)+","+str(j+1)] = "left"
        else:
            dict[str(i+1)+","+str(j+1)] = "diag"
        arr[i+1][j+1] = maxi
    else:
        upp = arr[i+1-1][j+1]-2
        left = arr[i+1][j+1-1]-2
        diag = arr[i+1-1][j+1-1]-1
        maxi = max(upp,left,diag)
        if maxi == upp:
            dict[str(i+1)+","+str(j+1)] = "upp"
        elif maxi == left:
            dict[str(i+1)+","+str(j+1)] = "left"
        else:
            dict[str(i+1)+","+str(j+1)] = "diag"
        arr[i+1][j+1] = maxi
    if((j+1)<len(s2)):
        rec(i,j+1)
    else:
        rec(i+1,0)

rec(0,0)
x = str(rows-1)+","+str(cols-1)
y = ""
while(x != "0,0"):
    temp = x.split(",")
    i = int(temp[0])
    j = int(temp[1])
    if(dict[x] == "diag"):
        y += s2[j-1]
        x = str(i-1)+","+str(j-1)
    elif dict[x] == "upp":
        y += "-"
        x = str(i-1)+","+str(j)
    else:
        y += "-"
        x = str(i)+","+str(j-1)

y = y[::-1]
print(y)
print(s2)