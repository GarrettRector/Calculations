def main():
    ans = input("Type > ")
    if ans.lower == "all":
        x = 0
        while True:
            x=x+1
            if x>1:
                for i in range(2,x):
                    if (x%i) == 0:
                        break
                else:
                    print(x)
    elif ans.lower == "range":
        rnge = input("Range > ")
        lower, upper = rnge.split(", ")
        for i in range(lower, upper + 1):
            if i > 1:
                for x in range(2, i):
                    if (i % i) == 0:
                        break
                else:
                    print(i)


while True:
    main()
