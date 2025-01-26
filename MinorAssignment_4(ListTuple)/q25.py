'''
Using the list given below
1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
Display a bar chart showing the response frequencies and their percentages of the total responses.

'''
def remove_duplicates(lst):
    # Loop through the list in reverse order to avoid skipping elements while modifying the list
    i = 0
    while i < len(lst):
        if lst[i] in lst[0:i]:  # Check if the current element has already appeared before
            lst.pop(i)  # Remove the duplicate element
        else:
            i += 1  # Move to the next element
    return lst

# Example usage:
my_list = [1, 2, 3, 2, 4, 3, 5]
remove_duplicates(my_list)
print(my_list) 

