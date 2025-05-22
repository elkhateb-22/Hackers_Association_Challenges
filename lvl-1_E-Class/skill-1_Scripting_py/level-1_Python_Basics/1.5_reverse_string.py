def reverse_string(input_str):
    reversed_str = ""
    for i in range(len(input_str) - 1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str

original_string = "rekcah_repus"
reversed_string = reverse_string(original_string)
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")