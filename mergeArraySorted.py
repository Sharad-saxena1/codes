arr1=[]
arr2=[]
n=int(input("Enter the value of n "))
print("Enter elements")
for i in range(n):
    e=int(input())
    arr1.append(e)
#print(arr1)
m=int(input("Enter the value of n "))
print("Enter elements")
for i in range(m):
    f=int(input())
    arr2.append(f)
#print(arr2)
def mergit(x,y):
    i=0
    j=0
    arr=[]
    while((i<n) and (j<m)):
        if x[i]<y[j]:
            arr.append(x[i])
            i+=1
        else:
            arr.append(y[j])
            j+=1
    while(i<n):
        arr.append(x[i])
        i+=1
    while(j<m):
        arr.append(y[j])
        j+=1
    return arr
print(mergit(arr1,arr2))