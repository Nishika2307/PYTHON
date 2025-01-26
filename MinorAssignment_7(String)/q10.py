'''
Write a script that reads a line of text as a string, tokenizes the string with the split method and outputs
the tokens in reverse order. Use space characters as delimiter
'''
def reverse_tokens(input_str):
    # Tokenize the string by splitting at spaces
    tokens = input_str.split()
    
    # Reverse the list of tokens
    reversed_tokens = tokens[::-1]
    
    # Join the reversed tokens back into a string and return
    return " ".join(reversed_tokens)

# Example usage
input_str = input("Enter a line of text: ")
reversed_str = reverse_tokens(input_str)
print(f"Reversed tokens: {reversed_str}")

'''
Enter a line of text: I am Nishika
Reversed tokens: Nishika am I'''
