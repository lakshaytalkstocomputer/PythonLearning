import decimal

grd_usd = None
while grd_usd is None:
    entry = input("GRD conversion: ")
    try:
        grd_usd = decimal.Decimal(entry)
    except decimal.InvalidOperation:
        print("Invalid: ", entry)
print(grd_usd , "GRD = 1 USD")

lunch = decimal.Decimal("12900")
lunch_in_dollar = lunch/grd_usd

print("Lunch Money in Dollars : " + str(lunch_in_dollar))
print()

penny = decimal.Decimal("0.00")
lunch_in_dollar = lunch_in_dollar.quantize(penny)

print("Lunch Money in Dollars : " + str(lunch_in_dollar))

bribe = (50000/grd_usd).quantize(penny)

print("Bribe payed = " + str(bribe))

cab = decimal.Decimal("23.50")

total_cost = lunch_in_dollar + bribe + cab

print("Total cost = " + str(total_cost))

