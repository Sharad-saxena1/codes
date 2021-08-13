arr=[]
ans=[]
n=int(input("Enter the value of n"))
print("Enter elements")
for i in range(n):
    e=input()
    arr.append(e)

def findDupli(x):
    for i in range(n):
        for j in range(i):
            if arr[i]==arr[j]:
                ans.append(arr[i])
    return ans
print(findDupli(arr))
