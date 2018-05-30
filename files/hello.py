def say_hello(name):
    print("Hello, " + name)


name = input("Please enter your name: ")

say_hello(name)

answer = input("Would you like another greeting? Y or N ")
if answer == 'Y' or answer == 'y':
    say_hello(name)
