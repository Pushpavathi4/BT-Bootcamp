
#Coding Challenge 40: Printing Pattern of Factorials in N Rows
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be a positive interger which is greater than 0.")
else:
    num=1
    prev=1
    for i in range(1,n+1):
        ans=""
        for j in range(0,i):
            ans+=str(prev)+" "
            prev=num*prev
            num+=1
        print(ans)