#Coding Challenge 24: Display the Series 1,1,2,3,5,8,13,21…N 
n = int(input("Enter n: "))

if n <= 0:
    print("Number should be positive integer greater than 0.")
else:
    a = 1
    b = 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b