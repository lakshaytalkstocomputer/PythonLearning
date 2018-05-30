age = int(input("PLease enter your age: "))

if age >= 21:
    print("You can buy Alcohol.")
if age >= 18:
    print("You can Vote.")
    print("You can have your driving license")
elif age >= 15:
    print("Sorry You cannot drink but you can learn Python.")