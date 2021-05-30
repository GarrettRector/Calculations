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
        nums = []
        while True:
            lowererr = False
            uppererr = False
            rnge = input("Range > ")
            lower, upper = rnge.split(", ")
            try:
                lower = int(lower)
            except ValueError as e:
                lowererr = True

            try:
                upper = int(upper)
            except ValueError as e:
                uppererr = True
            if lowererr or uppererr:
                if lowererr and uppererr:
                    print(f"{lower} and {upper} are both incorrect types. Integers only.")
                elif lowererr:
                    print(f"{lower} is incorrect type. Integers only.")
                elif uppererr:
                    print(f"{upper} is incorrect type. Integers only.")
            else:
                break
        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    nums.append(num)
        nums = str(nums)
        hold, nums = nums.split("[")
        nums, hold = nums.split("]")
        print(nums)
        num = None
        print("\n")
    elif ans.lower() == "prime":
        num = input("Number > ")
        num = int(num)
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    print(i, "times", num // i, "is", num)
                    break
            else:
                print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
        num = None
        print("\n")


while True:
    main()
