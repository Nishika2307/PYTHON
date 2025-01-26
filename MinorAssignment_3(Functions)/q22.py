'''
Create a function that prints the first 10 terms of an arithmetic progression.
'''
def print_ap_terms(first_term, common_difference):
    terms = [first_term + i*common_difference for i in range(10)]
    print("First 10 terms of the AP:", terms)


print_ap_terms(2, 3)

'''
First 10 terms of the AP: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
'''