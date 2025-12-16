#Coding Challenge 42: Generate Series - 1, -5, 9, -13, 17, -21, ... N 
n=int(input("Enter n:"))
if(n<=0):
    print("Number should be a positive interger which is greater than 0.")
else:
    num=1
    cnt=1
    while(num<=n):
        if(cnt%2==0):
            temp=-num
            print(temp,end=" ")
        else:
            print(num,end=" ")
        num+=4
        cnt+=1