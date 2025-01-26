'''
Write a function that takes a list of numbers as input from the user and produces the corresponding
cumulative list where each element in the list at index i is the sum of elements at index j ≤ i.
'''
def cumulative(lst):
    cumulative_list =[]
    total = 0
    for i in lst:
        total += i
        cumulative_list.append(total)
    print("Cumulative list:", cumulative_list)

# Input list
lst =[int(input("Enter an element : ")) for i in range(3)]
cumulative(lst)

'''
Enter list element 1: 3
Enter list element 2: 2
Enter list element 3: 1
Cumulative list: [3, 5, 6]
'''

       