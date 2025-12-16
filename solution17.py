#Coding Challenge 17: Display the Series 1,2,3,4,5,6…N

n=int(input("Enter n:"))
if(n<=0):
    print("Number should be positive integer greater than 0.")
for i in range(1,n+1):
    if(i==n):
        print(i)
    else:
        print(i,end=",")