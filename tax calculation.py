#tax calculation
Name=input("Enter the name of employee")
salary=float(input("Enter the salary"))
tax=0.10*salary
if(salary>50000):
    netsalary=salary-tax
    print("the salary of" +Name+ "is",salary)
    print("Taxable amount is ",netsalary)
else:
    print("the salary of" +Name+ "is",salary)
    print("tax is not aplicable")
    
