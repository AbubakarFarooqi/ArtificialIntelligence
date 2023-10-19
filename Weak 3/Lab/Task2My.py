def balance(s):
    bf = 0
    for i in range(len(s)):
        if s[i] == "(":
            bf +=1
        elif s[i] == ")":
            bf -= 1
    if bf == 0:
        return s
    if bf >0:
        for i in range(bf):
            s += ")"
    else:
        bf *=-1
        for i in range(bf):
            s = "(" + s
    return s

print(balance("(a + b (c)))"))