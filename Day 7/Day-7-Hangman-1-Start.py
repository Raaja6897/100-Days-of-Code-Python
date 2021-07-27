# Use the below link to see how the Hangman game works
# link = "https://en.wikipedia.org/wiki/Hangman_(game)"

import random

word_list=["lion", "raaja", "vignesh"]

word=random.choice(word_list)
print(word)
guess_word=input("Guess a word\n").lower()
for letter in word:
    if guess_word==letter:
        print("right")
    else:
        print("wrong")