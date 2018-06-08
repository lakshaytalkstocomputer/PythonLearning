amount = None
location = None

with open("message.txt", "r") as source:
    for line in source:
        clean = line.lower().rstrip()
        junk, pay, pay_data = clean.partition("pay")
        junk, meet, meet_data = clean.partition("rendezvous")
        if pay != '':
            amount = pay_data
        elif meet != "":
            location = meet_data
        else:
            pass

print("Budget", amount)
print("Meet :", location)
