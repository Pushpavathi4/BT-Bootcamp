#Coding Challenge 52: Level 1: Reverse the given array. 
arr=[3,2,4,66,54]
n=len(arr)
for i in range(0,n//2):
    temp=arr[i]
    arr[i]=arr[n-i-1]
    arr[n-i-1]=temp
print(arr)