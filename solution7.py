#Coding Challenge 7: Program to accept name and salary. Check if their salary is >3L and display if they must pay tax 
name=input("Enter your name:")
salary=input("Enter your salary:")
if(salary.replace(".","",1).isdigit()):
    salary=float(salary)
    if(salary<0):
        print("Salary cannot be negative!")
    elif(salary>300000):
        print(name,"must pay tax.")
    else:
        print(name,"does not need to pay tax.")
else:
    print("Invalid Salary! it should conatin only digits")