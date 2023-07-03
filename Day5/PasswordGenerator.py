import random

next_password = False
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
while not next_password:
    let = int(input("How many letters would you like in your password?\n"))
    sym = int(input("How many symbols would you like?\n"))
    num = int(input("How many numbers would you like?\n"))

    random_letters = str()
    random_symbols = str()
    random_numbers = str()

    for i in range(let):
        random_letters += random.choice(letters)
    for j in range(sym):
        random_symbols += random.choice(symbols)
    for k in range(num):
        random_numbers += random.choice(numbers)

    password = str(random_letters) + str(random_symbols) + str(random_numbers)
    random_password = random.sample(password, len(password))

    random.shuffle(random_password)
    password = ''.join(random_password)

    print(f"Here is your password: {password}")
    next_passwd = input("Do you wanna generate a new password? Type y/n:\n")
    if next_passwd == 'y':
        next_password = False
    else:
        next_password = True
