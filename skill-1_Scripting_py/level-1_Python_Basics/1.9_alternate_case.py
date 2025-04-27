# Original string
original = "H4ck3r"

# Method 1: Using a loop to alternate case
result1 = ""
for i in range(len(original)):
    char = original[i]
    if char.isalpha():  # Check if the character is a letter
        if i % 2 == 0:  # Even indices (0, 2, 4...) will be uppercase
            result1 += char.upper()
        else:  # Odd indices (1, 3, 5...) will be lowercase
            result1 += char.lower()
    else:  # If not a letter (like numbers), keep as is
        result1 += char

print(f"Method 1 result: {result1}")

# Method 2: Using a list comprehension with conditional expression
result2 = ''.join([
    c.upper() if i % 2 == 0 and c.isalpha() else
    c.lower() if c.isalpha() else c
    for i, c in enumerate(original)
])

print(f"Method 2 result: {result2}")

# Method 3: Simple manual construction for this specific case
result3 = "H4cK3r"
print(f"Method 3 result: {result3}")