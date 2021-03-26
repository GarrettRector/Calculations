
def main():
    # x coord
    while True:
        try:
            xp = input("X Coord : ")
            x = int(xp)
            break
        except:
            print("Incorrect Type. Try again")
            print(" ")
    while True:
        try:
            # y coord
            yp = input("Y Coord : ")
            y = int(yp)
            break
        except:
            print("Incorrect Type. Try again")
            print(" ")
    while True:
        try:
            # dilation factor
            dp = input("Dilation Factor : ")
            d2 = str(dp)
            try:
                d = float(dp)
                break
            except:
                one, two = d2.split("/")
                one1 = int(one)
                two2 = int(two)
                d = one1 / two2
                break
        except:
            print("Incorrect Type. Try again")
            print(" ")
    while True:
        try:
            # x for center of dilation
            op1 = input("Dilation center for X : ")
            o1 = int(op1)
            break
        except:
            print("Incorrect Type. Try again")
            print(" ")
    while True:
        try:
            # y for center of dilation
            op2 = input("Dilation center for Y : ")
            o2 = int(op2)
            break
        except:
            print("Incorrect Type. Try again")
            print(" ")

    xs1 = x - o1
    ys1 = y - o2
    xs2 = xs1 * d
    ys2 = ys1 * d
    xs3 = xs2 + o1
    ys3 = ys2 + o2
    print("Answer: ")
    print(f"({xs3} {ys3})")
    print(" ")


while True:
    main()
