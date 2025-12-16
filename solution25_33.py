#Retail Shopping Hackathon 
# ============================================
# Retail Shopping Application  Hackathon
# Coding Challenges 25 to 33 (Final Program)
# ============================================

PROMO_CODE = "PROMO10"

grand_total = 0
total_quantity = 0

print("\nWelcome to Retail Shopping System")

# ---------- ITEM ENTRY LOOP ----------
while True:
    item_code = input("\nEnter item code: ")
    description = input("Enter item description: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    item_total = quantity * price
    total_quantity += quantity

    # Promotional discount
    if item_code.upper() == PROMO_CODE:
        promo_discount = item_total * 0.10
        item_total -= promo_discount
        print("Promo Discount Applied (10%): ₹", promo_discount)
    else:
        promo_discount = 0

    grand_total += item_total
    print("Item Total: ₹", item_total)

    choice = input("Add another item? (y/n): ").lower()
    if choice != 'y':
        break

print("\n-------------------------------")
print("Original Grand Total: ₹", grand_total)
print("Total Quantity:", total_quantity)

# ---------- DISCOUNTS ----------
final_total = grand_total

# 10% discount on grand total
if final_total > 10000:
    discount_10 = final_total * 0.10
    final_total -= discount_10
    print("10% Discount Applied: ₹", discount_10)
else:
    discount_10 = 0

# 5% quantity discount
if total_quantity > 20:
    discount_5 = final_total * 0.05
    final_total -= discount_5
    print("5% Quantity Discount Applied: ₹", discount_5)
else:
    discount_5 = 0

# ---------- MEMBERSHIP DISCOUNT ----------
member = input("\nIs the customer a member? (y/n): ").lower()
if member == 'y':
    member_discount = final_total * 0.02
    final_total -= member_discount
    print("Membership Discount (2%): ₹", member_discount)
else:
    member_discount = 0
    print("No Membership Discount")

print("Total After Discounts: ₹", final_total)

# ---------- TAX CALCULATION ----------
if final_total < 5000:
    tax = final_total * 0.05
    tax_rate = "5%"
elif final_total <= 20000:
    tax = final_total * 0.10
    tax_rate = "10%"
else:
    tax = final_total * 0.15
    tax_rate = "15%"

total_after_tax = final_total + tax

print("\nTax Rate Applied:", tax_rate)
print("Tax Amount: ₹", tax)
print("Total After Tax: ₹", total_after_tax)

# ---------- PAYMENT MODE ----------
payment_method = input("\nSelect payment method (cash/card): ").lower()

if payment_method == "card":
    surcharge = total_after_tax * 0.02
    print("Credit Card Surcharge (2%): ₹", surcharge)
else:
    surcharge = 0
    print("Cash Payment No Surcharge")

final_payable = total_after_tax + surcharge

print("Final Payable Amount: ₹", final_payable)

# ---------- MINIMUM PURCHASE CHECK ----------
if final_payable < 500:
    print("\n Minimum purchase of ₹500 not met.")
    print("Invoice cannot be generated.")
    exit()

# ---------- LOYALTY POINTS ----------
loyalty_points = int(final_payable // 100)

# ---------- FINAL INVOICE ----------
print("\n======================================")
print("           FINAL INVOICE")
print("======================================")
print("Grand Total            : ₹", grand_total)
print("Total Discounts        : ₹", discount_10 + discount_5 + member_discount)
print("Tax                    : ₹", tax)
print("Surcharge              : ₹", surcharge)
print("--------------------------------------")
print("Final Amount Payable   : ₹", final_payable)
print("Loyalty Points Earned  :", loyalty_points)
print("======================================")
print("Thank you for shopping with us!")