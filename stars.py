for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print()

for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
print()

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
print()

for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
print()

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
print()

#
# for i in range(3):
#     for j in range(5 - i - 1):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()
# for i in range(5):
#     for j in range(5 - i - 1):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()
# print()