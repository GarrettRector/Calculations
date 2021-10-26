from colorama import Fore, init
init(autoreset=True)


def main():
    try:
        wavelength = float(input("Wavelength? > "))
        wavelength = wavelength/1e+9
    except ValueError:
        print(Fore.RED, "Wavelength has to be a integer or float")
        return
    ans = ((6.636 * 10 ** -34) * (3 * 10 ** 8)) / wavelength
    kj = input("Answer in kJ? > ")
    if "yes" in kj:
        print(Fore.GREEN, ans / 1000)
    else:
        print(Fore.GREEN, ans)
    return


if __name__ == "__main__":
    while True:
        main()
