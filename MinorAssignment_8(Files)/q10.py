'''
Write a Python function that reads a file file1 and displays the number of words and the number of
vowels in the file'''
# Writing a sample content to 'file1.txt'
with open("file1.txt", 'w') as file:
    file.write("hello , my name is mini googles . I am a resident of ohio \n and is very enthusiastic about rhymes")

# Reading the file and calculating word count and vowel count
def count_words_and_vowels(filename):
    with open(filename, 'r') as file:
        content= file.read()
        
        # Count words by splitting the content by space
        words=content.split()
        num_words = len(words)
        
        # Count vowels
        vowels = "aeiouAEIOU"
        num_vowels = 0  
        for i in content:
            if i in vowels:
                num_vowels+=1
                
        
        
        print(f"Number of words: {num_words}")
        print(f"Total count of vowels: {num_vowels}")

# Call the function for 'file1.txt'
count_words_and_vowels("file1.txt")
