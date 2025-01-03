start=int(input("Enter the number: "))
end=int(input("Enter the last number: "))
start2=int(input("Enter the number: "))
end2=int(input("Enter the last number: "))
for i in range(start,end):
    for j in range(start,i+1):
        print("*",end='')
    print()
for i in range (start2,end2):
    for j in range (i,end2):
        print("*",end='')
    print()    