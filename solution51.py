# the array of size n. 
n=int(input("Enter array size:"))
arr=[]
for i in range(n):
    val=int(input(f"Enter array element at {i} position:"))
    arr.append(val)
print(arr)