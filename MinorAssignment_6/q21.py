import pandas as pd
L = ['Cry', 'Apple', 'Orange', 'Sky', 'Banana']
# Convert list to Series
s = pd.Series(L)
# Elements with a vowel
vowel_series = s[s.str.contains(r'[aeiouAEIOU]')]
print("Series with vowels:", vowel_series)

# Elements starting with a vowel
start_vowel_series = s[s.str.match(r'^[aeiouAEIOU]')]
print("Series starting with a vowel:", start_vowel_series)


'''
str.contains(r'[aeiouAEIOU]'): This checks if each element contains at least one vowel (case-insensitive).
The regex [aeiouAEIOU] matches any of the vowels (a, e, i, o, u) in both uppercase and lowercase.
The resulting Series includes all elements containing at least one vowel.

str.match(r'^[aeiouAEIOU]'): This checks if each element starts with a vowel.
The ^ in the regex ensures that the match occurs at the beginning of the string.
The resulting Series includes all elements that start with a vowel.
'''