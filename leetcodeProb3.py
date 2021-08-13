nums = [1,97,9,85]
def find(x):
    l=len(x)
    p=x[0]
    k=1
    while k<l:
        if p>x[k]:
            k+=1
        else:
            p=x[k]
            k+=1
    for e in range(l):
        if p==x[e]:
            return e
print(find(nums))


