num=int(input("enter the number: "))
sum=0
while num:
    n=num%10
    sum+=n
    num=num//10
print("sum of the  number is: ", sum)