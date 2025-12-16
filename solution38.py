#Coding Challenge 38: Fibonacci Series Pattern (N Rows)
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be a positive interger which is greater than 0.")
else:
    a=1
    b=1
    for i in range(1,n+1):
        ans=""
        for j in range(0,i):
            ans+=str(a)+" "
            a,b=b,a+b
        print(ans)