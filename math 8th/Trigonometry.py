import math


def main():
    inp = input()
    typeOf, Type, angle = inp.split(" ")
    angle = float(angle)
    if (typeOf == "cos") & (Type == "rad"):
        print(f"cos {angle} = "'%.10s' % math.cos(angle))
    elif (typeOf == "sin") & (Type == "rad"):
        print(f"sin {angle} = "'%.10s' % math.sin(angle))
    elif (typeOf == "tan") & (Type == "rad"):
        print(f"tan {angle} = " + '%.10s' % math.tan(angle))
    elif typeOf == "side":
        inp = input("What side do you need? ")

    elif (typeOf == "cos") & (Type == "deg"):
        print(f"cos ({angle}) = {math.cos(math.radians(angle))}")
    elif (typeOf == "sin") & (Type == "deg"):
        print(f"sin ({angle}) = {math.sin(math.radians(angle))}")
    elif (typeOf == "tan") & (Type == "deg"):
        print(f"tan ({angle}) = {math.tan(math.radians(angle))}")


while True:
    main()
