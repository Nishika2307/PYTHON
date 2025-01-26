import numpy as np

# Generate a linearly spaced array
n = np.linspace(1.1, 6.6, num=6, endpoint=True, retstep=False, astype=['S'])
print(n, '\n')

# Reshape and convert the array to integers
n = n.reshape((2, 3)).astype(int)
# Print the reshaped array
print(n)

'''
[1.1 2.2 3.3 4.4 5.5 6.6] 

[[1 2 3]
 [4 5 6]]
 '''
 
'''
Arguments Breakdown:
1.1: The starting value of the sequence.
6.6: The ending value of the sequence.
num=6: Specifies that you want 6 evenly spaced values between 1.1 and 6.6, inclusive of the endpoint.
endpoint=True: This ensures that the last value in the sequence is included (i.e., 6.6 will be part of the output).
retstep=False: By default, retstep is False, which means the function will return only the values of the sequence, not the step size. If it were True, it would return both the values and the step size.
dtype=float: Specifies that the data type of the generated values should be float (which is the default behavior).''' 

 
