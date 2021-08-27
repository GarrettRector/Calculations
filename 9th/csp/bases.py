from string import ascii_lowercase


def main():
    while True:
        base = input("Converting from? ")
        tobase = input("To what base? ")
        try:
            base = int(base)
            break
        except ValueError:
            print(f'Either the base or the number is not a Integer. Try again')
    number = input("Number? ")
    if tobase == "10":
        answer = to_ten(base, number)
        print(answer)
    else:
        base_ten_val = to_ten(base, number)
        answer = from_ten(tobase, base_ten_val)
        print(answer)


def to_ten(base, number):
    ans = 0
    numbers = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=10)}
    for i in range(0, len(number)):
        num = number[i]
        if num.isalpha():
            num = [numbers.get(character) for character in num.lower()]
            num = str(num)[2:-2]
        n = len(str(number)) - (i + 1)
        pt1 = base ** n
        answer = int(num) * int(pt1)
        ans += int(answer)
    return ans


def from_ten(base, number):
    ans = ""
    while number > 0:
        ans += str(number % int(base))
        number = int(number/int(base))
    return ans[::-1]


if __name__ == '__main__':
    while True:
        main()
