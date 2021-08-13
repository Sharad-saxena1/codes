arr=[]
n=int(input("Enter the value of n "))
print("Enter elements")
for i in range(n):
    e=int(input())
    arr.append(e)
#print(arr)
def sortarr(x):
    l=0
    c=0
    h=len(x)-1
    while c<=h:
        if x[c]==0:
            x[c],x[l]=x[l],x[c]
            c+=1
            l+=1
        elif x[c]==1:
            c+=1
        else:
            x[c],x[h]=x[h],x[c]
            h-=1
    return x
print(sortarr(arr))
