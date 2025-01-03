'''def sum1(a):
    
    n=a%10
    n+=n
    sum1(a)
print(sum1(12345))'''
def sum(n):
       if n==0:
           return 0
       else:
           print(n%10)+sum(n//10)
n=12346
print("the sum of the number is :",(sum(n)))
