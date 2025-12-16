#Coding Challenge 5: Farmer Problem Statement 
#Total 80 acres , 5 segments equally divided so 16 acres
#Tomato , Potato , Cabbage , Sunflower , Sugarcane
acres=80/5

#tomato
tomato_30=0.3*acres*10
tomato_70=0.7*acres*12
tomato_yield=tomato_30+tomato_70
tomato_price=7*1000
tomato_revenue=tomato_price*tomato_yield

#potato
potato_yield=10*acres
potato_price=20*1000
potato_revenue=potato_price*potato_yield

#cabbage
cabbage_yield=14*acres
cabbage_price=24*1000
cabbage_revenue=cabbage_price*cabbage_yield

#sunflower
sunflower_yield=0.7*acres
sunflower_price=200*1000
sunflower_revenue=sunflower_price*sunflower_yield

#sugarcane
sugarcane_yield=45*acres
sugarcane_revenue=sugarcane_yield*4000

total_revenue=tomato_revenue+potato_revenue+cabbage_revenue+sunflower_revenue+sugarcane_revenue
revenue_11_months=total_revenue-sugarcane_revenue
print("The overall sales achieved by Mahesh from the 80 acres of land:",total_revenue)
print("Sales realisation from chemical-free farming at the end of 11 months:",revenue_11_months)