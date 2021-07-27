import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives=len(stages)-1


word_list = ["lion", "raaja", "vignesh"]

word = random.choice(word_list)
# creating "_" for the length of word
display_word = []
for i in range(len(word)):
    display_word.append("_")

print(word)
print(display_word)

game_over = False

while not game_over:
    guess_word = input("Guess a word\n").lower()
    for i in range(len(word)):
        letter = word[i]
        if letter == guess_word:
            display_word[i] = guess_word
    print(display_word)

    if guess_word not in word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose")

    if "_" not in display_word:
        game_over = True
        print("You win")

    print(stages[lives])
