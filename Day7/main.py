import random

word_list = ["aardvark", "baboon", "camel"]

choice = random.choice(word_list)
print(choice)

letter = input("Guess a letter: ").lower()

for i in range(len(choice)):
    if letter == choice[i]:
        print("Right")
    else:
        print("Wrong")