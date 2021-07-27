import random

word_list=["lion", "raaja", "vignesh"]

word=random.choice(word_list)
word_space=[]
for i in range(len(word)):
    word_space.append("_")

print(word)
print(word_space)
guess_word=input("Guess a word\n").lower()



right_wrong=[]
for letter in word:
    if guess_word==letter:
        right_wrong.append("right")
    else:
        right_wrong.append("wrong")

lst=right_wrong.copy()

for i in range(len(lst)):
    if lst[i]=="right":
        lst[i]=guess_word
    else:
        lst[i]="_"

print(lst)


