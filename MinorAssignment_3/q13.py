'''Write a program that converts a Roman numeral to its integer equivalent.'''
def roman_to_int(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(roman):
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value  # Subtract if smaller numeral comes before larger
        else:
            total += current_value  # Add if larger or equal numeral
        prev_value = current_value

    return total

# Get input from the user
roman = input("Enter a Roman numeral: ").upper()

# Convert and display the result
print(f"The integer equivalent of {roman} is {roman_to_int(roman)}")
