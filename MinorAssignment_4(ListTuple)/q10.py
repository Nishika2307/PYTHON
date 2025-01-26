'''
Write a Python function that takes a tuple of tuples and prints the sum of all numeric elements in the
inner tuples.
'''
def sum_of_inner_tuples(data):
    total_sum = 0
    for inner_tuple in data:
        for element in inner_tuple:
            if isinstance(element, (int, float)):  # Check if the element is numeric
                total_sum += element
    print(f"The sum of all numeric elements is: {total_sum}")


data = ((1, 4, 3), (4.5, 5, 'a'), (7.9, 8, 9))
sum_of_inner_tuples(data)


#The sum of all numeric elements is: 42.4