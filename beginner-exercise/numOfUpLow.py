def up_low(s):
    up = 0
    low = 0
    for char in s:
        if 'a' <= char <= 'z':
            low += 1
        elif 'A' <= char <= 'Z':
            up += 1
    print("Lower letter : ", low)
    print("Upper letter : ", up)


def up_low1(s):
    d = {"upper": 0,
         "lower": 0}
    for char in s:
        if char.islower():
            d["lower"] += 1
        elif char.isupper():
            d["upper"] += 1
    print("No of Lower letter : ", d["lower"])
    print("No of Upper letter : ", d["upper"])
