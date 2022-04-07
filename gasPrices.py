#Oscar Maldonado
#9/30/21
#gasPrices
from prettytable import PrettyTable
regular = input("What is the fuel type for regular? ")
plus = input("What is the fuel type for plus?       ")
premium = input("What is the fuel type for premium? ")
diesel = input("What is the fuel type for diesel?   ")
table = PrettyTable(['FuelType', 'Credit/Debit', 'Cash'])
table.add_row(['Regular', regular, round(float(regular) * 0.9, 2)])
table.add_row(['Plus', plus, round(float(plus) * 0.9, 2)])
table.add_row(['Premium', premium, round(float(premium) * 0.9, 2)])
table.add_row(['Diesel', diesel, round(float(diesel) * 0.9, 2)])
print(table)
