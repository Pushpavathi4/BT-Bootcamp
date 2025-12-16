#Coding Challenge 37: Printing number Increasing Pattern (N Rows)
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be a positive interger which is greater than 0.")
else:
    ans=""
    for i in range(1,n+1):
        ans+=str(i)
        print(ans)