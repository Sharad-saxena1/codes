s1=input()
s2=input()
def anaGra(x,y):
    x=x.replace(' ','').lower()
    y=y.replace(' ','').lower()

    if len(x)!=len(y):
        return False

    count ={}
    for i in x:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for i in y:
        if i in count:
            count[i]-=1
        else:
            count[i]=1
    for k in count:
        if count[k]!=0:
            return False
    return True
print(anaGra(s1,s2))