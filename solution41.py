#Coding Challenge 41: Convert Number to Words Using Mathematical Logic 
n=int(input("Enter n:"))
if(n<0):
    print("Number should be a positive interger which is greater than 0.")
else:
    dict={'0':"Zero",'1':"One",'2':"Two",'3':"Three",'4':"Four",'5':'Five','6':"Six",'7':"Seven",'8':"Eight",'9':"Nine",'10':"Ten"}
    for ch in str(n):
        print(dict[ch],end=" ")