'''
Write a function that takes n as an input and creates a list of n lists such that ith list contains first five
multiples of i.

'''
def create_multiples_list(n):
    result = []
    for i in range(1, n + 1):
        multiples = []
        for j in range(1, 6):
            multiples.append(i * j)
        result.append(multiples)
    return result

n = int(input("Enter the number of lists to create: "))
multiples_list = create_multiples_list(n)
for i in range(1, len(multiples_list) + 1):
    print(f"Multiples of {i}: {multiples_list[i-1]}")