z=int(input("Enter the 1st num: "))
y=int(input("Enter the 2nd num: "))
x=int(input("Enter the 3rd number "))
if(z<y<x):
    print("x is smallest value")
elif(z<x<y):
    print("y is smallest value")
elif(x<y<z):
    print("z is smallest value")
else:
    print("Give valid value")