#Coding Challenge 18: Display the Series 1,3,5,7,9…N 
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be positive integer greater than 0.")
for i in range(1,n+1,2):
    if(i==n-1 or i==n):
        print(i)
    else:
        print(i,end=",")