
def check_even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


try:
    number = int(input("Enter an integer: "))

    result = check_even_odd(number)

    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a valid integer.")
