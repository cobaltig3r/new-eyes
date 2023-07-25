weight = 22

# Ground Shipping

if weight <= 2:
  cost = str(weight * 1.50 + 20.00)
elif weight > 2 and weight <= 6:
  cost = str(weight * 3.00 + 20.00)
elif weight > 6 and weight <= 10:
  cost = str(weight * 4.00 + 20.00)
elif weight > 10:
  cost = str(weight * 4.75 + 20.00)
  
print("Ground Shipping Total: ", cost)

# Premium Ground shipping

cost = 125.00

print ("Ground Shipping Premium Total: " + str(cost))

# Drone Shipping

if weight <= 2:
  cost = str(weight * 4.50)
elif weight > 2 and weight <= 6:
  cost = str(weight * 9.00)
elif weight > 6 and weight <= 10:
  cost = str(weight * 12.00)
elif weight > 10:
  cost = str(weight * 14.25)

print("Drone Shipping Total: ", cost)
