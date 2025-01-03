def num(a):
    #a=[101,102,202,301,101]
    b=len(a)
    if a[0]==a[b-1]:
       return("true")
    else:
       return("false")
b=[101,202,30,30,23,101]
print(num(b))
