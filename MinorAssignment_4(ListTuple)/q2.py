'''
 Define a function rotate that receives three arguments and returns a tuple in which the first argument
is at index 1, the second argument is at index 2 and the third argument is at index 0. Define variables
a, b and c containing ’Doug’, 22 and 1984. Then call the function three times. For each call, unpack
its result into a, b and c, then display their values
'''
def rotate(a, b, c):
    return b, c, a
a, b, c = 'Doug', 22, 1984
for i in range(0,3,1):
    a, b, c = rotate(a, b, c)
    print(a, b, c)

'''
22 1984 Doug
1984 Doug 22
Doug 22 1984
'''

