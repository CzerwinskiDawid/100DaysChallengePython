import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
end_of_game = False
position = [rock, paper, scissors]
length = len(position)
rand_position = random.randint(0, length - 1)

while not end_of_game:
    your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

    if your_choice >= 3 or your_choice < 0:
        print("You typed an invalid number. You lose!")
    else:
        print(position[your_choice])
        print("\nComputer choose:\n")
        print(position[rand_position])

        if your_choice == rand_position:
            print("Draw")
        elif your_choice == 0 and rand_position == 1 or your_choice == 1 and rand_position == 2:
            print("You lose")
        else:
            print("You win")

    continue_game = input("Do you wanna play again? Type y/n:\n").lower()
    if continue_game == 'y':
        end_of_game = False
    else:
        end_of_game = True
