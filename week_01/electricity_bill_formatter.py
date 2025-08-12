full_name = input("Customer's full name:")
units_cosumed = int(input("Units consumed: kWh"))
cost = float(input("Cost per unit:" ))

total = units_cosumed * cost
print(f"{full_name}\n{units_cosumed}\n{total}")