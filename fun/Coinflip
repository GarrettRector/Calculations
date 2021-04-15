import random

def Average(lst):
    return sum(lst) / len(lst)

def cmd():
    while True:
        inp = input()
        try:
            cmd, times, amt = inp.split(" ")
            break
        except:
            cmd = inp
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
        print(f"Chance for Heads: {chance_head}/{amt} ({round(chance_head/int(amt)*100, 3)}%)")
        print(f"Chance for Tails: {chance_tail}/{amt} ({round(chance_tail/int(amt)*100, 3)}%)")

    if cmd == "avg":
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
        print(f"Average chance for heads:", round(average*100, 4))
        print(f"Average chance for tails:", round(avg*100, 4))

while True:
    cmd()
