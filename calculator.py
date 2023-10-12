#calculator for two numbers
cal=input("WELCOM IN THE VCMJ'S CALCULATER PRESS ENTER FOR CALCULATION")
print(cal)
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
print("choice1=sum",
      "choice2=subtract",
      "choice3=product",
      "choice4=divide")
choice=int(input("enter the choice 1,2,3 or 4"))
if(choice==1):
    print(num1+num2)
elif(choice==2):
    print(num1-num2)
elif(choice==3):
    print(num1*num2)
else:
    print(num1/num2)
