a=int(input("Enter the numbers: " ))
campare_Val=a
cubic=0
while a>0:
    n=a%10
    multi=n*n*n
    cubic+=multi
    a=a//10
if (cubic == campare_Val):
    print(cubic,"this is a amstrong number: ")
else:
    print(cubic,"this is not a  amstrong number")