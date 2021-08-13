def selectionSort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if (a[j]<a[min]):
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
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
print(selectionSort(arr))