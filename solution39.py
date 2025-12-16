#Coding Challenge 39: Printing Pattern of Perfect Squares with Alternating Signs in N Rows
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be a positive interger which is greater than 0.")
else:
    num=1
    for i in range(1,n+1):
        ans=""
        for j in range(0,i):
            if(num%2==0):
                ans+="-"
            ans+=str(num*num)+" "
            num+=1
        print(ans)