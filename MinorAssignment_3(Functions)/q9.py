'''
Write two functions, one of which converts a binary number to decimal and the other one does the
reverse.'''

def dec_bin(n,c):
    if(n==0):
     return 0
    else:
       return (n%2)* 10**c +dec_bin(n//2,c+1)
    #(a%2,end="")


def bin_dec(n,c):
   if(n==0):
    return 0
   return n%10 * 2**c +bin_dec(n//10,c+1)

print(f"Decimal to Binary ",dec_bin(6,0))
print("Binary to Decimal ",bin_dec(110,0))

'''
Decimal to Binary  110
Binary to Decimal  6
'''