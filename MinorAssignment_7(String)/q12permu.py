'''
Write a script that reads a five-letter word from the user and produces every possible three-letter
string, based on the word’s letters. For example, the three-letter words produced from the word
“bathe” include “ate,” “bat,” “bet,” “tab,” “hat,” “the,” and “tea.” Challenge: Investigate the functions
from the itertools module, then use an appropriate function to automate this task
'''
import itertools as it

def generate_three_letter_words(word):
    # Generate all possible 3-letter permutations from the word
    permutations =it.permutations(word, 3)
    three_letter_words = []
    # Convert each permutation tuple to a string and collect them
    for p in permutations:
         three_letter_words.append(''.join(p))
        
    # Remove duplicates by converting the list to a set
    unique_words = set(three_letter_words)
    
    return unique_words

# Get a five-letter word from the user
word = input("Enter a five-letter word: ")

# Check if the word is exactly five letters
if len(word) == 5:
    # Generate three-letter words and print them
    three_letter_words = generate_three_letter_words(word)
    print(f"Three-letter words: {', '.join(sorted(three_letter_words))}")
else:
    print("Please enter exactly a five-letter word.")
