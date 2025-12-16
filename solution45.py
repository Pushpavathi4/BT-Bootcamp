# Working with Arrays 
# Coding Challenge 45: Level 0: Write a program to accept n and store the elements into 
# the array of size n. 
n=int(input("Enter array size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter array element at {i} position:"))
    arr.append(val)
print(arr)