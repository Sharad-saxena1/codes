def insertionSort(a):
    n=len(a)
    for i in range(1,n):
        j=i-1
        key=a[i]
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a

arr=[]
x= int(input("Enter the len of array"))
arr=[]
print("enter elements")
for i in range(x):
    data=int(input())
    arr.append(data)
print(arr)
print("array after sorting")
print(insertionSort(arr))