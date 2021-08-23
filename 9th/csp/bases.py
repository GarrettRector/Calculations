def main():
    inp = input("To or From Base 10 > ")
    match inp.lower():
        case "to":
            ans = 0
            while True:
                base = input("Converting from? ")
                number = input("Number? ")
                try:
                    base = int(base)
                    break
                except ValueError:
                    print(f'Either the base or the number is not a Integer. Try again')
            for i in range(0, len(number)):
                num = str(number)[i]
                n = len(number) - (i+1)
                pt1 = base ** n
                answer = int(num) * int(pt1)
                ans += int(answer)
            print(ans)

        case "from":
            pass
        case _:
            print("Unknown command")


if __name__ == '__main__':
    while True:
        main()
