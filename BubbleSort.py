def Bubblesort(a):
    n=len(a)
    s=0
    for i in range(n-1):
        print("pass = {0}".format(i+1))
        s=1
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                s=0
        if (s):
            return a
    return a

x= int(input("Enter the len of array"))
arr=[]
print("enter elements")
for i in range(x):
    data=int(input())
    arr.append(data)
print(arr)
print("array after sorting")
print(Bubblesort(arr))