#Coding Challenge 44: Reverse of a number 
# Write a program to find the reverse of a number. Store the reverse value in a different variable. 
# Display the reverse. 
n=int(input("Enter a number:"))
is_negative=n<0
n=abs(n)
temp=0
while(n>0):
    digit=n%10
    n//=10
    temp=temp*10+digit
if(is_negative):
    temp=-temp
print(temp)