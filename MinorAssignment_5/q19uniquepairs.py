'''
Given a long list of words, write a Python function unique pairs(words) to find all unique pairs
of words that:
• Have no common letters (e.g., "cat" and "dogs" have no letters in common).
2
Centre for Data Science
Institute of Technical Education & Research, SOA, Deemed to be University
• Each word in the pair should have at least 4 letters.
• Each unique pair should be stored in a set as a tuple in lexicographical order.
The function should return a set of all such unique pairs. Example:
words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))
'''


def unique_pairs(words):
    # Filter words with at least 4 letters
    words = [word for word in words if len(word) >= 4]
    
    # Initialize a set to store unique pairs
    unique_pairs_set = set()
    
    # Iterate through all pairs of words
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1, word2 = words[i], words[j]
            
            # Check if the two words have no common letters
            if not set(word1) & set(word2):
                # Create the tuple in lexicographical order and add to the set
                pair = tuple(sorted([word1, word2]))
                unique_pairs_set.add(pair)
    
    return unique_pairs_set

# Example usage:
words = ["apple", "dogs", "cat", "bird", "fish", "zebra", "lion"]
print(unique_pairs(words))

'''
{('apple', 'dogs'), ('fish', 'zebra'), ('apple', 'fish'), ('dogs', 'zebra'), ('lion', 'zebra'), ('apple', 'bird')}'''
