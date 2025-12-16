#Coding Challenge 54: Level 3: Implement Binary Search on the array. 
n=int(input("Enter Array Size:"))
arr=[]

for i in range(n):
    arr.append(int(input(f"Enter element {i}:")))

arr.sort()

print("Sorted array:",arr)

low=0
high=n-1
target=int(input("Enter target element:"))
found=False
while(low<=high):
    mid=(low+high)//2
    if(arr[mid]==target):
        found=True
        print(f"{target} found at index {mid}.")
        break
    elif(target<arr[mid]):
        high=mid-1
    else:
        low=mid+1

if(not found):
    print(f"{target} element not found in the array")