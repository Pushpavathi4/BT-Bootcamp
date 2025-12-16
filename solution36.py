#Coding Challenge 36: Printing number Increasing Pattern (N Rows)
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be a positive interger which is greater than 0.")
else:
    for i in range(1,n+1):
        ans=""
        for j in range(0,i):
           ans+=str(i)
        print(ans)
