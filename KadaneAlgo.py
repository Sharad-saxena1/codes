arr=[]
n=int(input("Enter the value of n "))
print("Enter elements")
for i in range(n):
    e=int(input())
    arr.append(e)
def kadane(x):
    c=x[0]
    g=x[0]
    for i in range(n-1):
        c=max(x[i],c+x[i])
        if c>g:
            g=c
    return g
print(kadane(arr))