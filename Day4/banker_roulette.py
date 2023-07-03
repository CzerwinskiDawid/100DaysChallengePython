import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length_of_list = len(names)
random_num = random.randint(0, length_of_list - 1)
who_pays = names[random_num]
print(f"{who_pays} is going to buy the meal today!")
