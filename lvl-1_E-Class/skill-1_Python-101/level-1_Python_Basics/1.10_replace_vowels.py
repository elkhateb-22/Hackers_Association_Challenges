# Original password
password = "P@ssw0rd"

# Method 1: Using a for loop
result1 = ""
vowels = "aeiouAEIOU"
for char in password:
    if char in vowels:
        result1 += "*"
    else:
        result1 += char
print(f"Method 1: {result1}")

# Method 2: Using string replace() for each vowel
result2 = password
for vowel in "aeiouAEIOU":
    result2 = result2.replace(vowel, "*")
print(f"Method 2: {result2}")

# Method 3: Using regular expressions
import re
result3 = re.sub(r'[aeiouAEIOU]', '*', password)
print(f"Method 3: {result3}")

# Method 4: Using translate with a translation table
vowel_map = str.maketrans({
    'a': '*', 'e': '*', 'i': '*', 'o': '*', 'u': '*',
    'A': '*', 'E': '*', 'I': '*', 'O': '*', 'U': '*'
})
result4 = password.translate(vowel_map)
print(f"Method 4: {result4}")