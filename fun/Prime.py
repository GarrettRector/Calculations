def main():
    ans = input("Type > ")
    if ans.lower() == "all":
        x = 0
        while True:
            x = x + 1
            if x > 1:
                for i in range(2, x):
                    if (x % i) == 0:
                        break
                else:
                    print(x)
    elif ans.lower() == "range":
        while True:
            rnge = input("Range > ")
            uppererr = False
            lowererr = False
            lower, upper = rnge.split(", ")
            try:
                lower = int(lower)
                break
            except:
                lowererr = True
            try:
                upper = int(upper)
                break
            except:
                uppererr = True
            if lowererr or uppererr:
                if lowererr and uppererr:
                    print(f"{lower} and {upper} are both incorrect types. Integers only.")
                elif lowererr:
                    print(f"{lower} is incorrect type. Integers only.")
                elif uppererr:
                    print(f"{upper} is incorrect type. Integers only.")
        upper = int(upper)
        for i in range(lower, upper + 1):
            if i > 1:
                for x in range(2, i):
                    if (i % i) == 0:
                        break
                else:
                    print(i)


while True:
    main()
