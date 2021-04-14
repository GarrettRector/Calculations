import numpy
import math


def main():
    inp = input()
    typeOf, Type, angle = inp.split(" ")
    angle = float(angle)
    if (typeOf == "cos") & (Type == "rad"):
        print(f"cos{angle} = "'%.10s' % math.cos(angle))
    elif (typeOf == "sin") & (Type == "rad"):
        print(f"sin{angle} = "'%.10s' % math.sin(angle))
    elif (typeOf == "tan") & (Type == "rad"):
        print(f"tan '%.10s'{angle} = " + '%.10s' % math.tan(angle))
    elif typeOf == "radical":
        inp = input("What side do you have? ")
        if inp == "short":
            print("short")
    elif (typeOf == "cos") & (Type == "deg"):
        print(f"cos ({angle}) = " + numpy.degrees(numpy.cos(angle)))
    elif (typeOf == "sin") & (Type == "deg"):
        print(f"sin ({angle}) = " + numpy.degrees(numpy.sin(angle)))
    elif (typeOf == "tan") & (Type == "deg"):
        print(f"tan({angle}) = " + numpy.degrees(numpy.tan(angle)))
        
        
while True:
    main()
