
medicines=["Para","Cold syrup","vicks choclate","Pain killer"]
cusname=input("Enter the name: ")
no_buys=int(input("Enter the  quantity no:"))
a=[]
b=[]
for i in range (no_buys):
    buys=input("Enter your medicince name: ")
    amount=int(input("Enter the amount: "))
    a.append(buys)
    b.append(amount)




c=sum(b)
if buys in medicines:
    d=",".join(a)
    z=",".join(map(str,b))
   
    m1=open("bill.txt", "w")
    m1.write(f"customer name :{cusname}\nNo of quantity: {no_buys}\n")
    m1.write(f"Medicines buys and total: {d}\nRs:{z}\nTotoal price: {c}")
   
    m1=open("bill.txt","r")
    print(m1.read())
    print("Thank You!!!")
    m1.close()
else:
    "Get well soon"
