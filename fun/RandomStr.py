import random
import time


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


def infinity():
    while True:
        yield


usedstr = []
fstrings = []

inp = input("Gui? ")
if inp == "gui":
    fstring = ""
    for _ in range(10):
        for i in range(15):
            for n in range(2 ** (i + 1)):
                randstring = random_string_generator(i + 1, ("A", "B"))
                if randstring not in usedstr:
                    print(randstring)
                    usedstr.append(randstring)
                else:
                    n = n - 1
        for _ in range(10):
            for i in range(10):
                string = usedstr[(i * i) ** 2]
                try:
                    strings = string[i]
                except IndexError:
                    pass
                print(strings)
                fstring = fstring + strings
            print(fstring)
            fstrings.append(fstring)
            fstring = ""
            count = usedstr.count(fstring)
            print(f"String is only in the list {count} time")
    print("Done!")
    time.sleep(1)
    print("Generating new strings!")
    time.sleep(.5)
    fstring = ""
    for i in range(10):
        print(fstrings[i])
elif inp == "no gui":
    fstring = ""
    for _ in range(10):
        for i in range(15):
            for n in range(2 ** (i + 1)):
                randstring = random_string_generator(i + 1, ("A", "B"))
                if randstring not in usedstr:
                    usedstr.append(randstring)
                else:
                    n = n - 1
        for _ in range(10):
            for i in range(10):
                string = usedstr[(i * i) ** 2]
                try:
                    strings = string[i]
                except IndexError:
                    pass
                print(strings)
                fstring = fstring + strings
            print(fstring)
            fstrings.append(fstring)
            fstring = ""
            count = usedstr.count(fstring)
            print(f"String is only in the list {count} time")
    print("Done!")
    time.sleep(1)
    print("Generating new strings!")
    time.sleep(.5)
    fstring = ""
    for i in range(10):
        print(fstrings[i])
