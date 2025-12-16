#Coding Challenge 20: Display the Series 1,2,4,7,11,16,22…N 
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be positive integer greater than 0.")
else:
    curremt=1
    increment=0
    while(curremt<=n):
        print(curremt,end=" ")
        increment+=1
        curremt+=increment
