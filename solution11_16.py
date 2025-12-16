#Tax Calculator Problem Hackathon  

#Coding Challenge 16: Input Validation Rules 
def validate_name():
    while True:
        name=input("Enter employee name:").strip()
        if name and name.replace(" ","").isalpha() and len(name)<=50:
            return name
        else:
            print("Ivalid name. Use alphabets only (max 50 characters).")

def validate_empid():
    while True:
        emp_id = input("Enter employee Id: ").strip()
        if emp_id.isalnum() and 5 <= len(emp_id) <= 10:
            return emp_id
        else:
            print("Invalid EmpID. Use alphanumeric (5–10 characters).")

def validate_basic_salary():
    while True:
        try:
            value = float(input("Enter basic monthly salary: "))
            if 0 < value <= 10000000:
                return value
            else:
                print("Basic salary must be positive and ≤ ₹1,00,00,000.")
        except ValueError:
            print("Enter a numeric value.")

def validate_allowance():
    while True:
        try:
            value = float(input("Enter special allowances: "))
            if 0 <= value <= 10000000:
                return value
            else:
                print("Allowance must be ≥ 0 and ≤ ₹1,00,00,000.")
        except ValueError:
            print("Enter a numeric value.")
    
def validate_bonus():
    while True:
        try:
            value = float(input("Enter Bonus percentage: "))
            if 0 <= value <= 100:
                return value
            else:
                print("Bonus percentage must be between 0 and 100.")
        except ValueError:
            print("Enter a numeric value.")

#Coding Challenge 11: Basic Input and Salary Calculation
employee_name=validate_name()
employee_id=validate_empid()

basic_monthly_salary=validate_basic_salary()
special_allowances=validate_allowance()
bonus_percentage=validate_bonus()

gross_monthly_salary=basic_monthly_salary+special_allowances

if gross_monthly_salary<=0:
    print("Gross Monthly Salary must be greater than zero.")
    exit()

annua_without_bonus=gross_monthly_salary*12
bonus_amount=(bonus_percentage/100)*annua_without_bonus
annual_gross=annua_without_bonus+bonus_amount

if annual_gross > 10000000:
    print("Annual Gross Salary exceeds realistic limit.")
    exit()

# print()
# print("-----Employee Deatils-----")
# print(f"Employee Name:{employee_name}")
# print(f"Employee Id:{employee_id}")
# print(f"Gross Monthly Salary:{gross_monthly_salary}")
# print(f"Annual Gross Salary:{annual_gross}")

#Coding Challenge 12: Taxable Income Calculation 
standard_deduction=50000
taxable_income=annual_gross-standard_deduction
# print()
# print("Annual Gross salary:",annual_gross)
# print("Standard Deduction:",standard_deduction)
# print("Taxable Income:",taxable_income)

#Coding Challenge 13: Tax and Rebate Calculation 

tax=0

if(taxable_income<=700000):
    tax=0
    print("\nSection 87A Rebate Applied (tax=0)")
else:
    if taxable_income>300000:
        tax+=min(300000,taxable_income-300000)*0.05
    
    if taxable_income>600000:
        tax+=min(300000,taxable_income-600000)*0.10

    if taxable_income>900000:
        tax+=min(300000,taxable_income-900000)*0.15

    if taxable_income>1200000:
        tax+=min(300000,taxable_income-1200000)*0.20
    
    if taxable_income>1500000:
        tax+=min(taxable_income-300000)*0.30

cess=tax*0.04
total_tax=tax+cess 

# print("\n------Tax Calaculation------")
# print("Taxable Income:",taxable_income)
# print("Income Tax:",tax)
# print("Health & Education Cess (4%):",cess)
# print("Total Tax Payable:",total_tax)

#Coding Challenge 14: Net Salary Calculation
net_salary=annual_gross-total_tax
# print("\n------Net Salary Calculation-------")
# print("Annual Salary:",annual_gross)
# print("Total Tax Payable:",total_tax)
# print("Annual Net Salary:",net_salary)

#Coding Challenge 15: Report Generation 
# Coding Challenge 15: Report Generation

print("\n" + "="*40)
print("          EMPLOYEE TAX REPORT")
print("="*40)

print("\nEmployee Details")
print("-"*40)
print("Name                 :", employee_name)
print("Employee ID          :", employee_id)

print("\nSalary Details")
print("-"*40)
print("Gross Monthly Salary :", "₹", gross_monthly_salary)
print("Annual Gross Salary  :", "₹", annual_gross)

print("\nTax Details")
print("-"*40)
print("Taxable Income       :", "₹", taxable_income)
print("Income Tax           :", "₹", tax)
print("Health & Edu Cess    :", "₹", cess)
print("Total Tax Payable    :", "₹", total_tax)

print("\nNet Salary")
print("-"*40)
print("Annual Net Salary    :", "₹", net_salary)

print("\n" + "="*40)