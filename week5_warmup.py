# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic="abracadabra"
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet='abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:12:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote="Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy  "
print(quote[83:-1])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
python="Python is fun. Fun is good. Good is subjective."
print(python.find("subjective"))
print(python[36:-1])
# b. Extract every third word.
words=python.split()
every_third_word=words[::3]
result=' '.join(every_third_word)
print(result)
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
split_python=["Python", "is", "fun", "Fun", "is", "good", "Good", "is", "subjective"]
print(split_python[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
starwars="MAY THE FORCE BE WITH YOU"
print(starwars.lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
life= "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(life.replace("busy", "distracted"))
# b. Replace "plans" with "mistakes".
print(life.replace("plans", "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
conc="Iteration"*7
print(conc)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quote2="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
quotemoon=False
print("The quote has the word moonlight? "+str(quotemoon))
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
phrase="Supercalifragilisticexpialidocious"
print(phrase.find("Supercalifragilisticexpialidocious"))
# b. Count the number of times the letter 'i' appears in the same word/phrase. 
print(len(phrase))