print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
couple = name1 + name2

T = couple.count('t')
R = couple.count('r')
U = couple.count('u')
E = couple.count('e')

total_T = T + R + U + E

L = couple.count('l')
O = couple.count('o')
V = couple.count('v')
E = couple.count('e')

total_L = L + O + V + E

total_as_string = int(str(total_T) + str(total_L))

if total_as_string < 10 or total_as_string > 90:
    print(f"Your score is {total_as_string}, you go together like coke and mentos.")
elif 40 <= total_as_string <= 50:
    print(f"Your score is {total_as_string}, you are alright together.")
else:
    print(f"Your score is {total_as_string}.")