#Coding Challenge 9: Program to check if a year given is a leap year or not 
year=int(input("Enter year:"))
if(year%400==0):
    print(year,"is a Leap Year")
elif(year%100==0):
    print(year,"is not a Leap Year")
elif(year%4==0):
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")