#Sals Shipping

weight = 1.5

#Ground Shipping
premium_g_shipping = 125
  
print("Get Ground Shipping Premium for $"+ str(premium_g_shipping))

flat_charge = 20
if weight <= 2:
   totalcost= weight * 1.50 + flat_charge
elif weight <= 6:
   totalcost= weight * 3 + flat_charge
elif weight <= 10:
  totalcost= weight * 4 + flat_charge   
else:
  weight >= 10
  totalcost= weight * 4.75 + flat_charge
print("Total Ground shipping cost: $",totalcost)

  #Drone Shipping

if weight <= 2:
    weight = weight * 4.50
elif weight <= 6:
   weight = weight * 9
elif weight <= 10: 
   weight = weight * 12
else:
   weight >= 10
   weight = weight * 14.25
print("Total Drone Shipping cost: $",weight) 






