num=int(input("enter the number:"))
i=1
fact=0
while(i<=num):
    if(num%i==0):
        fact=fact+1
    i=i+1
if(fact==2):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
