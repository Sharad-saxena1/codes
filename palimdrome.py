def pali(x):
    real=x
    s=0
    while(x>0):
        d=x%10
        s=s*10+d
        x//=10
    print(s)

    if (real==s):
       return True
    else:
        return False
print(pali(232))