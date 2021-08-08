import random


def str_gen(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for _ in range(str_size))


usedstr = []
fstrings = []


def main():
    while True:
        inp = input("Gui? ")
        if inp.lower() == "gui":
            fstring = ""
            for _ in range(10):
                for i in range(15):
                    for _ in range(2 ** (i + 1)):
                        randstring = str_gen(i + 1, ("A", "B"))
                        if randstring not in usedstr:
                            print(randstring)
                            usedstr.append(randstring)
                        else:
                            _ -= 1
                for _ in range(10):
                    for i in range(10):
                        string = usedstr[(i * i) ** 2]
                        try:
                            strings = string[i]
                            print(strings)
                            fstring = fstring + strings
                        except IndexError:
                            print("err")
                    print(fstring)
                    fstrings.append(fstring)
                    fstring = ""
                    count = usedstr.count(fstring)
                    print(f"String is only in the list {count} time")
            print("Done!")
            print("Generating new strings!")
            for i in range(10):
                print(fstrings[i])
        else:
            fstring = ""
            for _ in range(10):
                for i in range(15):
                    for n in range(2 ** (i + 1)):
                        randstring = str_gen(i + 1, ("A", "B"))
                        if randstring not in usedstr:
                            usedstr.append(randstring)
                        else:
                            n = n - 1
                for _ in range(10):
                    for i in range(10):
                        string = usedstr[(i * i) ** 2]
                        try:
                            strings = string[i]
                            print(strings)
                            fstring = fstring + strings
                        except IndexError:
                            pass
                    print(fstring)
                    fstrings.append(fstring)
                    fstring = ""
                    count = usedstr.count(fstring)
                    print(f"String is only in the list {count} time")
            print("Done!")
            print("Generating new strings!")
            for i in range(10):
                print(fstrings[i])


if __name__ == '__main__':
    main()
