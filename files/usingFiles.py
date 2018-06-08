with open("message.txt", "w") as target:
    print("Message to HQ", file=target)
    print("Device size 10 31/32", file=target)

with open("message.txt", "a") as target:
    target.write("hello\nhello")

with open("message.txt", "r") as source:
    text = source.read()


with open("message.txt", "r") as source1:
    for line in source1:
        print(line, end="")


with open("message.txt", "r") as source2:
    for line in source2:
        junk1, keyword, size = line.rstrip().partition("size")
        if keyword != '':
            print(size)
