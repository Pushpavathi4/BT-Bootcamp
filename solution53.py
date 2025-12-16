# Coding Challenge 53: Level 2: Sort the array in ascending or descending order based 
# on input of user 
n=int(input("Enter array size:"))
if(n<=0):
    print("size of the array should be positive greater than 0.")
else:
    arr=[]
    for i in range(n):
        val=int(input(f"Enter array element at {i} position:"))
        arr.append(val)
    print("Original Array:",arr)
    ascending_order = sorted(arr)
    print("Ascending Order:",ascending_order)
    descending_order=sorted(arr,reverse=True)
    print("Descending Order:",descending_order)
