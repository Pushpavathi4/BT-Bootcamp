#Coding Challenge 49: Level 4: Search the given element from the array 
arr=[4,2,34,89,7]
n=int(input("Enter search element:"))
find=arr.count(n)
if(find):
    print("element found")
else:
    print("element not present in the array")