n = int(input("Enter a number: "))
total_sum = 0  # To store the sum of all intermediate sums
digit_sum = 0  # To store the sum of the digits of each iteration

while n > 9:
    # Reset digit_sum for each iteration
    digit_sum = 0
    temp = n
    
    # Calculate sum of digits of the current number
    while temp != 0:
        digit_sum += temp % 10
        temp = temp // 10
    
    # Add digit_sum to total_sum
    total_sum += digit_sum
    
    # Update n with the new sum of digits
    n = digit_sum

# Output the final total_sum
print(total_sum)

'''
o/p
Enter a number: 123
6'''
