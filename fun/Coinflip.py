import random


def Average(lst):
    return sum(lst) / len(lst)


def cmd():
    global times, inp, amt, chance
    while True:
        inp = input()
        try:
            cmd, times, amt = inp.split(" ")
            break
        except ValueError:
            try:
                cmd, amt = inp.split(" ")
                break
            except ValueError:
                cmd = inp
                times = 1
                amt = 1
                break
    if cmd == "flip":
        chance_head = 0
        chance_tail = 0
        for i in range(int(amt)):
            check = 0
            ranum = random.randint(0, 1)
            if ranum == 0:
                chance_head += 1
            elif ranum == 1:
                chance_tail += 1
            if (chance_head | chance_tail == int(amt) / 2) & (check == 0):
                print("Halfway done!")
                check = 1
        print(f"Chance for Heads: {chance_head}/{amt} ({round(chance_head / int(amt) * 100, 3)}%)")
        print(f"Chance for Tails: {chance_tail}/{amt} ({round(chance_tail / int(amt) * 100, 3)}%)")
    elif cmd == "avg":
        listh = []
        listt = []
        for i in range(int(times)):
            chance_head = 0
            chance_tail = 0
            for i in range(int(amt)):
                ranum = random.randint(0, 1)
                if ranum == 0:
                    chance_head += 1
                elif ranum == 1:
                    chance_tail += 1
            listh.append(chance_head / int(amt))
            listt.append(chance_tail / int(amt))
        average = Average(listh)
        avg = Average(listt)
        print(f"Average chance for heads:", round(average * 100, 4))
        print(f"Average chance for tails:", round(avg * 100, 4))
        listh.clear()
        listt.clear()
    elif cmd == "luck":
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


while True:
    cmd()
