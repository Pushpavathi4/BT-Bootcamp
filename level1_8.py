#Setting the Scene: A Day at HealWell Care Hospital 
# ---------- LEVEL 7: ADMIN SETUP ----------
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

# Safety check
if len(services) != len(costs):
    print("Service and cost mismatch.")
    exit()

# ---------- LEVEL 1: PATIENT DETAILS ----------
print("\nHealWell Care Hospital")

name = input("Enter patient name: ")
age = int(input("Enter age: "))
gender = input("Enter gender: ")
contact = input("Enter contact number: ")

# ---------- LEVEL 2: DISPLAY SERVICES ----------
print("\nAvailable Services:")
for i in range(len(services)):
    print(f"{i+1}. {services[i]}")

choices = input("\nEnter service numbers (comma separated): ")

selected_services = []
selected_costs = []

choice_list = choices.split(",")

# ---------- LEVEL 3: FETCH COSTS ----------
for choice in choice_list:
    index = int(choice.strip()) - 1
    if 0 <= index < len(services):
        selected_services.append(services[index])
        selected_costs.append(costs[index])

# ---------- LEVEL 4: SUBTOTAL ----------
total_cost = sum(selected_costs)

# ---------- LEVEL 8: DISCOUNTS ----------
discounted_subtotal = total_cost
senior_discount = 0
high_bill_discount = 0

if age >= 60:
    senior_discount = discounted_subtotal * 0.10
    discounted_subtotal -= senior_discount

if discounted_subtotal > 5000:
    high_bill_discount = discounted_subtotal * 0.05
    discounted_subtotal -= high_bill_discount

# ---------- LEVEL 5: GST ----------
gst = discounted_subtotal * 0.18
grand_total = discounted_subtotal + gst

# ---------- LEVEL 6: INVOICE ----------
print("\n-----------------------------------------------")
print("HealWell Care Hospital")
print("Patient Invoice")
print("-----------------------------------------------")

print("\nPatient Information:")
print("Name:", name)
print("Age:", age)
print("Gender:", gender)
print("Contact:", contact)

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i+1}. {selected_services[i]}: ₹{selected_costs[i]}")

print("\nSubtotal: ₹", total_cost)

if senior_discount > 0:
    print("Senior Citizen Discount (10%): -₹", senior_discount)

if high_bill_discount > 0:
    print("High-Bill Discount (5%): -₹", high_bill_discount)

print("Subtotal After Discounts: ₹", discounted_subtotal)
print("GST (18%): ₹", gst)
print("Grand Total: ₹", grand_total)

print("\nThank you for choosing HealWell Care Hospital!")
print("-----------------------------------------------")