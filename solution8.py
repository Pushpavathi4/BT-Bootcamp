#Coding Challenge 8: To find the largest of 3 numbers
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if(a>=b and a>=c):
    print(a,"is the largest of 3 numbers")
elif(b>=a and b>=c):
    print(b,"is the largest of 3 numbers")
else:
    print(c,"is the largest of 3 numbers")
#print(max(a,b,c),"is the largest of 3 numbers")

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