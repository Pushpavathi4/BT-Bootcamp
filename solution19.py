#Coding Challenge 19: Display the Series 4,16,36,64…N 
n=int(input("Enter n:"))
if(n<=1):
    print("Number should be positive integer greater than 1.")
else:
    for i in range(2,n+1,2):
        print(i*i,end=" ")
