arr = ["tortilla", "cheese", "meat", "MORE MEAT"]  # init array
for _, i in enumerate(iter(bool, True)):
    inp = input("Taco? > ")
    if "taco" in inp:
        print(arr[_]) if _ <= 3 else print(arr[3])
