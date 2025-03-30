import math

def square_root(x):
    if x < 0:
        print("Error: Square root of a negative number is not defined in real numbers.")
        return None
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        print("Error: Factorial of a negative number is not defined")
        return None
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        print("Error: Natural logarithm is only defined for positive numbers.")
        return None
    return math.log(x)

def power(x, y):
    return math.pow(x, y)

# comment 3
if __name__ == "__main__":
    while True:
        print("Scientific Calculator")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Log (ln(x))")
        print("4. Power (xʸ)")
        print("5. Exit")

        choice = int(input("Enter choice: "))
        if choice in [1, 2, 3, 4]:
            num = float(input("Enter number: "))
            if choice == 1:
                print("Result:", square_root(num))
            elif choice == 2:
                print("Result:", factorial(int(num)))
            elif choice == 3:
                print("Result:", natural_log(num))
            elif choice == 4:
                num2 = float(input("Enter exponent: "))
                print("Result:", power(num, num2))
        elif choice == 5:
                break
        else:
            print("Invalid choice")
