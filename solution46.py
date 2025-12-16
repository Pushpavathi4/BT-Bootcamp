#Coding Challenge 46: Level 1: Find the Sum of all elements in the array 
n=int(input("Enter array size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter array element at {i} position:"))
    arr.append(val)
print(arr)

sum=0
for i in range(n):
    sum+=arr[i]
print("Sum of array elements:",sum)