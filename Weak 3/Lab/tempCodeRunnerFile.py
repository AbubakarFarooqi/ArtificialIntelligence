x = str(rows-2)+","+str(cols-2)
y = ""
while(x != "0,0"):
    temp = x.split(",")
    print(temp)
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


print(dict)
print(y)