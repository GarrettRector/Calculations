for i, _ in enumerate(iter(bool, True)):
    inp = input("Taco? > ")
    if "taco" in inp: print(["tortilla", "cheese", "meat", "MORE MEAT"][i]) if i <= 3 else print(arr[3])
