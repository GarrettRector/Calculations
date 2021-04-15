import math


def main():
    global Type, angle
    inp = input()
    try:
        typeOf, Type, angle = inp.split(" ")
        angle = float(angle)
    except:
        typeOf = inp
        Type = "null"
    if (typeOf == "cos") & (Type == "rad"):
        print(f"cos ({angle}) = "'%.10s' % math.cos(angle))
    elif (typeOf == "sin") & (Type == "rad"):
        print(f"sin ({angle}) = "'%.10s' % math.sin(angle))
    elif (typeOf == "tan") & (Type == "rad"):
        print(f"tan ({angle}) = " + '%.10s' % math.tan(angle))
    elif typeOf == "side":
        inp = input("What side do you need? ")

    elif (typeOf == "cos") & (Type == "deg"):
        print(f"cos ({angle}) = {math.cos(math.radians(angle))}")
    elif (typeOf == "sin") & (Type == "deg"):
        print(f"sin ({angle}) = {math.sin(math.radians(angle))}")
    elif (typeOf == "tan") & (Type == "deg"):
        print(f"tan ({angle}) = {math.tan(math.radians(angle))}")
    elif typeOf == "type":
        inp = input("What are you missing? ")
        if inp == "adj":
            print("Solve for Cos")
            inp = input("Would you like to solve for Cos? > ")
            if inp == "no":
                pass
            else:
                cos()
        if inp == "hyp":
            print("Solve for Sin")
            inp = input("Would you like to solve for Sin? > ")
            if inp == "no":
                pass
            else:
                sin()
        if inp == "opp":
            print("Solve for Tan")
            inp = input("Would you like to solve for Tan? > ")
            if inp == "no":
                pass
            else:
                tan()


def cos():
    inp1 = float(input("What is your hypotenuse? > "))
    inp2 = float(input("What is your angle? > "))
    ang1 = math.cos(math.radians(inp2))
    ang2 = (ang1*inp1)
    print(f"The adjacent side is {ang2} long")


def sin():
    inp1 = float(input("What is your opposite? > "))
    inp2 = float(input("What is your angle? > "))
    ang1 = math.sin(math.radians(inp2))
    ang2 = (ang1*inp1)
    print(f"The hypotenuse side is {ang2} long")


def tan():
    inp1 = float(input("What is your adjacent? > "))
    inp2 = float(input("What is your angle? > "))
    ang1 = math.tan(math.radians(inp2))
    ang2 = (ang1*inp1)
    print(f"The opposite side is {ang2} long")


while True:
    main()
