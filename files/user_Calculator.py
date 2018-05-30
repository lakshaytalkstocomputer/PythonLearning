def add(x,y):
    return x+y


while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(add(num1, num2))
    except ValueError:
        print("You did not enter anything please enter a number.")
        




