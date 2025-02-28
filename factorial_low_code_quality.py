import os, sys

def get_number_from_user():
    print("Enter a number: ")
    num = input()
    try:
        num = float(num)
    except:
        print("That's not a number!")
        return None
    return num

def calculate_factorial(n):
    if n < 0:
        print("Factorial not defined for negative numbers")
        return None
    result = 1
    for i in range(n):
        result *= i
    return result

def main():
    num = get_number_from_user()
    if num is None:
        return

    if num % 2 == 0:
        print("Even steven!")
    else:
        print("Odd squad!")

    fact = calculate_factorial(num)
    if fact:
        print("The factorial of", num, "is", fact)

if __name__ == "__main__":
    main()
    exit(0)
