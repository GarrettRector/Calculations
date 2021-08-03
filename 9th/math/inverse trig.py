import math


def main():
    global Type, angle, num
    inp = input()
    try:
        typeOf, Type, angle = inp.split(" ")
        angle = float(angle)
    except:
        try:
            typeOf, num = inp.split(" ")
            Type = "null"
        except:
            typeOf = inp
            Type = "null"
            
       # normal block
    if (typeOf.lower() == "cos") & (Type.lower() == "rad"):
        print(f"cos ({angle}) = "'%.10s' % math.cos(angle))
    elif (typeOf.lower() == "sin") & (Type.lower() == "rad"):
        print(f"sin ({angle}) = "'%.10s' % math.sin(angle))
    elif (typeOf.lower() == "tan") & (Type.lower() == "rad"):
        print(f"tan ({angle}) = " + '%.10s' % math.tan(angle))
        
        # inverse block
    elif (typeOf.lower() == "cos") & (Type.lower() == "deg"):
        print(f"cos ({angle}) = {math.cos(math.radians(angle))}")
    elif (typeOf.lower() == "sin") & (Type.lower() == "deg"):
        print(f"sin ({angle}) = {math.sin(math.radians(angle))}")
    elif (typeOf.lower() == "tan") & (Type.lower() == "deg"):
        print(f"tan ({angle}) = {math.tan(math.radians(angle))}")
    elif typeOf.lower() == "type":
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
    elif typeOf.lower() == "simplify":
        rad1 = int(num)
        workrad1 = rad1
        sqrnum = 1

        for i in range(2, rad1):
            mexp = 1
            while i ** mexp <= workrad1:
                if workrad1 % i ** mexp == 0:
                    mexp = mexp + 1
                else:
                    break
            if mexp > 2:
                sqrfac = i ** (int((mexp - 1) / 2))
                sqrnum = sqrnum * sqrfac
                workrad1 = workrad1 / (sqrfac ** 2)

        outsidenum = int(sqrnum)
        insidenum = int(rad1 / (sqrnum ** 2))
        print("The square root of " + str(rad1) + " is"),
        if insidenum == 1:
            print(outsidenum)
        else:
            if outsidenum == 1:
                print("√" + str(insidenum))
            else:
                print(str(outsidenum) + "√" + str(insidenum))
    elif typeOf.lower() == "help":
        print("Cmds are:\nSin, Cos, and Tan, all of which can be used with either rad or deg to get your different function. The 3rd arguement should be the number you want to be passed in\n"
              "There is also a function to find if you need to use sin cos or tan. The command for this is type.\n"
              "A radical simplifier is also built in, which can be used with simplify and then what you want to simplify\n")
    elif typeOf.lower() == "inverse":
      math.degrees(math.acos())

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
