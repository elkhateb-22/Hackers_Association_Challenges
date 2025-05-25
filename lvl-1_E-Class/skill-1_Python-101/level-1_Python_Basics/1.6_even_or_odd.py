def is_even_or_odd(number):
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

try:
    user_number = int(input("Enter a number to check if it's even or odd: "))
    result = is_even_or_odd(user_number)
    print(f"{user_number} is {result}")
except ValueError:
    print("Please enter a valid integer.")
