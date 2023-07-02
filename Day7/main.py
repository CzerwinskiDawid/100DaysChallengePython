import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
length = len(chosen_word)

print(f"{chosen_word}")

display = []
for i in range(length):
    display += "_"

guess = input("Guess a letter: ").lower()

for position in range(length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
