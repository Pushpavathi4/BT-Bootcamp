#Coding Challenge 50: Level 5: Display the number of odd and even numbers from the array
arr=[0,2,4,5,3,1,8,77]
odd_count=0
even_count=0
for i in arr:
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1

print(f"Odd count:{odd_count},Even count:{even_count}")
