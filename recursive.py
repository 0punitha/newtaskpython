def Fact(x):
    if x==1:
        return 1
    else:
        return x*Fact(x-1)
n="1235"
print(Fact(n))
    