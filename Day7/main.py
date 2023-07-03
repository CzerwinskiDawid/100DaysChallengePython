import random
import hangman_art
import hangman_words

stages = hangman_art.stages

end_of_games = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
length = len(chosen_word)
lives = 6

print(hangman_art.logo)

print(f"{chosen_word}")

display = []
for i in range(length):
    display += "_"

while not end_of_games:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_games = True
            print("You lose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_games = True
        print("You win")

    print(stages[lives])
