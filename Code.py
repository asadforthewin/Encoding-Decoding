import random

# Define a list of random strings
random_str = ["hah", "gao", "qrw", "aab", "ava", "abc", "ave", "aey", "rye"]

# Take user input for a message
x = input("Enter your message: ")

# Ask the user to choose coding (1) or decoding (0)
coding = input("Press 1 for coding and 0 for decoding")
coding = True if (coding == "1") else False

# Initialize an empty list to store words after coding/decoding
words_direc = []

# Check if the user chose coding
if coding:
    for word in x.split(" "):
        # For words with a length of 3 or more characters, swap first and last characters
        if len(word) >= 3:
            new_word = random.choice(random_str) + word[1:-1] + word[0] + random.choice(random_str)
            words_direc.append(new_word)
        else:
            # For words with less than 3 characters, reverse the word
            words_direc.append(word[::-1])

else:
    # If the user chose decoding
    for word in x.split(" "):
        if len(word) >= 3:
            # For words with a length of 3 or more characters, reverse the swap
            new_word = word[-1] + word[1:-1] + word[0]
            words_direc.append(new_word)
        else:
            # For words with less than 3 characters, reverse the word
            words_direc.append(word[::-1])

# Print the result by joining the words in the words_direc list with spaces
print(" ".join(words_direc))