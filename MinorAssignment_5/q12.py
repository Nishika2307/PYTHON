'''
Write a program that uses a dictionary to determine and print the number of duplicate words in a
sentence. Treat uppercase and lowercase letters the same and assume there is no punctuation in the
sentence
'''
# Taking user input for the sentence
sentence = input("Enter a sentence: ")

# Converting the sentence to lowercase to handle case insensitivity
sentence = sentence.lower()

# Splitting the sentence into words
words = sentence.split()

# Initialize an empty dictionary to count word occurrences
word_count = {}

# Counting the occurrences of each word
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

# Finding and printing duplicate words (those with more than 1 occurrence)
duplicates = {word: count for word,count in word_count.items() if count > 1}

print("Duplicate words and their counts:", duplicates)

'''
Enter a sentence: Apple and apple
Duplicate words and their counts: {'apple': 2}
'''