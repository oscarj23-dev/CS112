
#Oscar Maldonado
#Lab #2
#9/29/2021


# Here I am declaring some variables such as the checkout items and their prices

applePrice = 1
orangePrice = 2.50
milkPrice = 3.99
cookiePrice = 6.78
tax = .08
appleNum = 2
orangeNum = 1
milkNum = 3
cookieNum = 2

# Here are a couple print statements for the reciept
print("How many apples are you purchasing? ", str(appleNum))
print()
print("How many oranges are you purchasing? ", str(orangeNum))
print()
print("How many gallons of milk are you purchasing? ", str(milkNum))
print()
print("How many cookies are you purchasing? ", str(cookieNum))
print()
print()
print()
print("********************************************************************")
print("                      Thank you for shopping at")
print("                           Grocery store")
print("                             9/28/2021")
print()
print("Item                 Price               Quantity            total")
print()

# Here I made the calculations for the totals of the fruits based on how many items they got
appleTotal = appleNum * applePrice
orangeTotal = orangeNum * orangePrice
milkTotal = milkNum * milkPrice
cookieTotal = cookieNum * cookiePrice
grossTotal = appleTotal + orangeTotal + milkTotal + cookieTotal
print("Apples               $", str(applePrice),"               ", str(appleNum), "                  $", str(appleTotal))
print("Apples               $", str(orangePrice),"             ", str(orangeNum), "                  $", str(orangeTotal))
print("Apples               $", str(milkPrice),"            ", str(milkNum), "                  $", str(milkTotal))
print("Apples               $", str(cookiePrice),"            ", str(cookieNum), "                  $", str(cookieTotal))
print("Total                                                        $", str(grossTotal))
print("Tax                                                          $", str(round(grossTotal * tax, 2)))
print("Total after tax                                              $", str(grossTotal + round(grossTotal * tax, 2)))
# Here I decided to do the calculations for the tax and such in the print statements
# Because I did not like how redundant the program was becoming in all honest it was 
# Making me mad





