'''
Twenty students were asked to rate on a scale of 1 to 5 the quality of the food in the student cafeteria,
with 1 being “awful” and 5 being “excellent.” Place the 20 responses in a list.
1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5
Determine and display the frequency of each rating. Use the built-in functions, statistics module
functions and NumPy functions to display the following response s: minimum, maximum,
range, mean, median, mode, variance and standard deviation
'''
from collections import Counter
import statistics as s

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
freq = Counter(responses)

print("Frequencies:", freq)
print("Minimum:", min(responses))
print("Maximum:", max(responses))
print("Range:", max(responses) - min(responses))
print("Mean:", s.mean(responses))
print("Median:", s.median(responses))
print("Mode:", s.mode(responses))
print("Variance:", s.variance(responses))
print("Standard Deviation:", s.stdev(responses))

'''
Frequencies: Counter({3: 8, 2: 4, 1: 3, 5: 3, 4: 2})
Minimum: 1
Maximum: 5
Range: 4
Mean: 2.9
Median: 3.0
Mode: 3
Variance: 1.568421052631579
Standard Deviation: 1.2523661815266247'''
