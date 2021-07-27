import random

word_list = ["lion", "raaja", "vignesh"]

word = random.choice(word_list)
# creating "_" for the length of word
display_word = []
for i in range(len(word)):
    display_word.append("_")

print(word)
print(display_word)

game_over=False

while not game_over:
    guess_word = input("Guess a word\n").lower()
    for i in range(len(word)):
        letter = word[i]
        if letter == guess_word:
            display_word[i] = guess_word
    print(display_word)

    if "_" not in display_word:
        game_over = True
        print("You win")
