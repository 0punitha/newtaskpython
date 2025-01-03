'''import csv

with open ("Example.csv",'w') as f1:
    w=csv.writer(f1)
    w.writerow(["s.no","Name","Company","Salary"])
    no=int(input("Enter the number of Employee's: "))

for x in range (no):
    a=int(input("Enter the seral number:"))
    b=input("Enter thr name: ")
    c=input("Enter the company name: ")
    d=float(input("Enter the Salary: "))
    w.writerow([a,b,c,d])'''

import csv

f1=open("Example1.csv","w", newline="")
w=csv.writer(f1)
w.writerow(["s.no","Dress_type","Cloth_type","Per dress rate"])
no=int(input("Enter the quantity: "))
for i in range (no):
    s_no=int(input("Enter the no: "))
    cloth_type=input("Enter the  cloth type: ")
    Dress_type=input("Enter the dress model: ")
    rs=int(input("Enter the Rs: "))
    w.writerow([s_no,Dress_type,cloth_type,rs])
f1.close()

#Reading the file
f1=open("Example1.csv","r")
r1=csv.reader(f1)
for i in r1:
    print(i)
f1.close()