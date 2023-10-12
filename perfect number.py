num=int(input("Enter the number"))
i=1
fact=0
while(i<num):
    if(num%i==0):
        fact=fact+i
    i=i+1
if(fact==num):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
    
    
