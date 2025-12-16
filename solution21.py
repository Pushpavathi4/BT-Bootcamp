
#Coding Challenge 21: Display the Series 1,4,9,25,36,49,81…N 
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be positive integer greater than 0.")
else:
    for i in range(1,n+1):
        if(i%4!=0):
            print(i*i,end=" ")