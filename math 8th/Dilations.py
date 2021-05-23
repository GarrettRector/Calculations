def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def main():
    # x coord
    while True:
        try:
            xp = input("X Coord : ")
            x = float(xp)
            break
        except:
            print("Incorrect Type. Try again")
            print(" ")
    while True:
        try:
            # y coord
            yp = input("Y Coord : ")
            y = float(yp)
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
            o1 = float(op1)
            break
        except:
            print("Incorrect Type. Try again")
            print(" ")
    while True:
        try:
            # y for center of dilation
            op2 = input("Dilation center for Y : ")
            o2 = float(op2)
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
    ys4 = int(abs(ys3))
    ys4 = str(abs(ys4))
    xs4 = int(abs(xs3))
    xs4 = str(abs(xs4))
    xs5 = truncate(xs4, 4+len(xs4))
    ys5 = truncate(ys4, 4+len(ys4))
    print("Answer:")
    if "00" in xs5 or ys5:
        print(f"({int(float(xs5))}, {int(float(ys5))})")
    else:
        print(f"({xs5}, {ys5})")
    print("")


while True:
    main()
