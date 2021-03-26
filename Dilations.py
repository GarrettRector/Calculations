
def main():
    # x coord
    xp = input("X Coord : ")
    x = int(xp)
    # y coord
    yp = input("Y Coord : ")
    y = int(yp)
    # dilation factor
    dp = input("Dilation Factor : ")
    d2 = str(dp)
    try:
        d = float(dp)
    except:
        one, two = d2.split("/")
        one1 = int(one)
        two2 = int(two)
        d = one1 / two2
    # x for center of dilation
    op1 = input("Dilation center for X : ")
    o1 = int(op1)
    # y for center of dilation
    op2 = input("Dilation center for Y : ")
    o2 = int(op2)

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
