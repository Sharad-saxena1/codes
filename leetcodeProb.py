s = "bbbaaaba"
t = "aaabbbab"
c = 0
e = 0
b = []
d = []
sl = len(s)
tl = len(t)
if (sl == tl):
    for i in range(sl):
        for j in range(sl):
            if s[i] == s[j]:
                c = c+1
                b.append(j)

            if t[i] == t[j]:
                e += 1
                d.append(j)
    if(c == e) and (b == d):
        print("True")
    else:
        print("False")
else:
    print("enter equal length of string")
print(c,b,e,d,sl,tl)
