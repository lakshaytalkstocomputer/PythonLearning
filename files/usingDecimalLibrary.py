""" FLOATING POINT NUMBERS are an approximation. We can't rely on approximation
So we have to use decimal.Decimal Library
"""


from decimal import Decimal

conversion = Decimal("247.78")
print(conversion)
lunch = Decimal("12900")
lunch_in_dollar = lunch/conversion

print("Lunch Money in Dollars : " + str(lunch_in_dollar))
print()

""" All those digits are a consequence of exact division: we got a lot of 
decimal places of precision, not all of them are really relevent.

To, round off, we will use quantize method.
Quantize means rounding up , rounding down, and truncating a given value.
"""

penny = Decimal("0.00")
lunch_in_dollar = lunch_in_dollar.quantize(penny)

print("Lunch Money in Dollars : " + str(lunch_in_dollar))

bribe = (50000/conversion).quantize(penny)

print("Bribe payed = " + str(bribe))

cab = Decimal("23.50")

total_cost = lunch_in_dollar + bribe + cab

print("Total cost = " + str(total_cost))
