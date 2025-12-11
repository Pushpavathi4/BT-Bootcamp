#Program to calculate the discount on the total amount
total_amount=float(input("Enter total amount:"))
discount_percent=float(input("Enter discount percent:"))
if(total_amount>=0 and discount_percent>=0 and discount_percent<=100):
    disounted_amount=total_amount*discount_percent/100
    after_discount=total_amount-disounted_amount
    print("Discounted amount:", disounted_amount)
    print("Final amount:", after_discount)
else:
    print("Invalid Discount Percent")