# TODO
import re
import cs50
import sys

gg = 0


def main():
    lol = cs50.get_int("Number: ")
    lol = str(lol)
    if len(lol) == 15:
        AMEX(lol)
    elif len(lol) == 13:
        VISA(lol)
    elif len(lol) ==16:
        help(lol)
    else:
        invalid()


def AMEX(lol):
    for i in [34,37]:
        a = str(i)
        pattern = re.compile(a)
        if pattern.search(lol, 0, 2) != None:

            if checksum(lol) == True:
                print("AMEX")
                sys.exit(0)

    invalid()

def invalid():
    print("INVALID")
    sys.exit(0)

def VISA(lol):
    for i in [4]:
        a = str(i)
        pattern = re.compile(a)
        if pattern.search(lol, 0) != None:
                if checksum(lol) == True:
                    print("VISA")
                    sys.exit(0)
    invalid()

def MAC(lol):
    for i in [51,52,53,54,55]:
        a = str(i)
        pattern = re.compile(a)
        if pattern.search(lol, 0, 2) != None:
                if checksum(lol) == True:
                    print("MASTERCARD")
                    sys.exit(0)
    invalid()

def help(lol):
    if lol[0] == "4":
        VISA(lol)
    else:
        MAC(lol)

def checksum(lol):
    check = 0
    bro = len(lol)
    see = int(lol)

    for i in range(bro):
        if (i + 1)%2 == 0:
            z = 2*(see%10)
            if z >= 10:
                z = 1 + z%10
        else:
            z = see%10
        check += z
        see = see//10

    if check%10 == 0:
        return True
    else:
        return False




if __name__ == "__main__":
    main()