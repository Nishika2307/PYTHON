'''
Write a function that receives a list of words, then determines and displays in alphabetical order only
the unique words. Treat uppercase and lowercase letters as the same. The function should use a set to
get the unique words in the list. Test your function with several sentences.
'''
sentence= input("Enter the first sentence: ")
sentence = sentence.lower()
words = sentence.split()
unique_sorted_words = sorted(set(words))
print("Unique words in alphabetical order:", unique_sorted_words)

'''
Enter the third sentence:  apple grapes grapes orange orange
Unique words in alphabetical order: ['apple', 'grapes', 'orange']'''
