
def multi(a,b):
    c=a*b
    if(c<=1000):
        return(c)
    else:
        return(a+b)
x=int(input("Enter the value:"))
y=int(input("Enter the value:"))
z=multi(x,y)
print("The result is:",z)