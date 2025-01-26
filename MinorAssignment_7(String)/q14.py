'''
14. Write a Python program to reverse the middle half of characters in a string.'''

s = input("Enter a string: ")
n = len(s)
start=n // 4
end =3 * n // 4
r=s[start:end]
reverse=r[::-1]
result = s[:start] + reverse + s[end:]
print("Result:", result)






'''
Divide the string into quarters:

n // 4: This is the starting index of the second quarter of the string (the beginning of the middle half).
3 * n // 4: This is the ending index of the third quarter (the end of the middle half).
Why n // 4 and 3 * n // 4?

A string can be conceptually divided into four parts:
First quarter
Second quarter (start of middle half)
Third quarter (end of middle half)
Fourth quarter
To reverse the middle half, you take the second and third quarters, which are from n // 4 to 3 * n // 4.
Examples:

If the string has 8 characters (abcdefgh):
n = 8
n // 4 = 2, 3 * n // 4 = 6
Middle half: Characters from index 2 to 6 ("cdef")'''