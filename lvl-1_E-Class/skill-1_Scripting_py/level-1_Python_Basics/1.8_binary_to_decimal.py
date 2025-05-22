# Define the binary string
binary_string = "100101"

# Method 1: Using built-in int() function with base 2
decimal_value = int(binary_string, 2)
print(f"The decimal value of {binary_string} is: {decimal_value}")

# Method 2: Manual conversion for learning purposes
def binary_to_decimal_manual(binary_str):
    decimal = 0
    # Iterate through each digit, starting from right to left
    for i in range(len(binary_str)):
        # Get position from right
        power = len(binary_str) - 1 - i
        # Add value if digit is '1'
        if binary_str[i] == '1':
            decimal += 2 ** power
    return decimal

manual_result = binary_to_decimal_manual(binary_string)
print(f"Manual conversion result: {manual_result}")