# TODO
from cs50 import get_int

lol = get_int("Height: ")

while lol > 8 or lol < 1:
    lol = get_int("Height: ")

for i in range(lol):
    for j in range(lol - (i + 1)):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end ="")
    print("  ", end ="")
    for m in range(i + 1):
        print("#", end ="")
    print("\n", end ="")