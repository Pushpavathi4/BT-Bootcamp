# Program to calculate Simple Interest

# Input values
principal = float(input("Enter Principal amount: "))
rate = float(input("Enter Rate of Interest (in %): "))
time = float(input("Enter Time (in years): "))

# Simple Interest formula
simple_interest = (principal * rate * time) / 100

# Output
print("Simple Interest =", simple_interest)
