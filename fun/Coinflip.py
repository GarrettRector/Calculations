import random


def cmd():
    global times, inp, amt, chance
    while True:
        print("Options:\n* flip\n* avg\n* luck")
        inp = input()
        try:
            command, times, amt = inp.split(" ")
            break
        except ValueError:
            try:
                command, amt = inp.split(" ")
                break
            except ValueError:
                times = 1
                amt = 1
                break
    if "flip" in inp:
        chance_head = 0
        chance_tail = 0
        for _ in range(int(amt)):
            ranum = random.randint(0, 1)
            if ranum == 0:
                chance_head += 1
            elif ranum == 1:
                chance_tail += 1
        print(f"Chance for Heads: {chance_head}/{amt} ({round(chance_head / int(amt) * 100, 3)}%)\nChance for Tails: "
              f"{chance_tail}/{amt} ({round(chance_tail / int(amt) * 100, 3)}%)")
    elif "avg" in inp:
        listh = []
        listt = []
        for _ in range(int(times)):
            chance_head, chance_tail = 0, 0
            for _ in range(int(amt)):
                ranum = random.randint(0, 1)
                chance_head += 1 if ranum == 0 else chance_tail + 1
            listh.append(chance_head / int(amt))
            listt.append(chance_tail / int(amt))
        average = sum(listh)/len(listh)
        avg = sum(listt)/len(listt)
        print(f"Average chance for heads: {round(average * 100, 4)}\nAverage chance for tails: {round(avg * 100, 4)}")
        listh.clear(), listt.clear()
    elif "luck" in inp:
        left = int(times)
        chancelist = []
        chances = 0
        while True:
            if left != 0:
                chance = 100
                for i in range(left):
                    flip = random.randint(0, 1)
                    if flip == 0:
                        left = left - 1
                        chances = chances + 1
                        chancelist.append(left)
                    elif flip == 1:
                        chances = chances + 1
                        chancelist.append(left)
            else:
                break
        chance = 100
        for i in range(chances):
            chance = chance / 2
        print(f"The chance of that set happening was {chance}%")
        hold, chance = str(chancelist).split("[")
        chance, hold = str(chance).split("]")
        print(chance)
        chancelist.clear()
    else:
        print("Invalid input")
        cmd()


if __name__ == '__main__':
    cmd()
