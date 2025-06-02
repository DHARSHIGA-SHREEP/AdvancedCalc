import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot compute square root of a negative number."
    return math.sqrt(x)

def logarithm(x, base=10):
    if x <= 0:
        return "Error: Logarithm undefined for non-positive values."
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("Advanced Calculator")
    print("-------------------")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Exit")

    while True:
        choice = input("\nEnter choice (1-11): ")

        if choice == '11':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {power(num1, num2)}")

        elif choice == '6':
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            print(f"Result: {square_root(num)}")

        elif choice == '7':
            try:
                num = float(input("Enter number: "))
                base = float(input("Enter base (default is 10): ") or 10)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            print(f"Result: {logarithm(num, base)}")

        elif choice in ('8', '9', '10'):
            try:
                angle = float(input("Enter angle in degrees: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue

            if choice == '8':
                print(f"Result: {sine(angle)}")
            elif choice == '9':
                print(f"Result: {cosine(angle)}")
            elif choice == '10':
                print(f"Result: {tangent(angle)}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    calculator()
