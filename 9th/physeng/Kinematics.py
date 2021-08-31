from sympy import solve, symbols


def main():
    inp = input('Choose an equation. If you do not know the equations type "help" > ')
    match inp.lower():
        case "1":
            solving = input("What are you solving for? > ")
            match solving.lower():
                case "time":
                    while True:
                        try:
                            d = input("Distance? > ")
                            d = float(d)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((vf + vi) / 2) * x - d, x)
                    print(answer)
                case "vi":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            d = input("Distance? > ")
                            d = float(d)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((vf + x) / 2) * t - d, x)
                    print(answer)
                case "vf":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            d = input("Distance? > ")
                            d = float(d)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((x + vi) / 2) * t - d, x)
                    print(answer)
                case "d":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    answer = ((vi + vf) / 2) * t
                    print(f"distance is {answer}")
        case "2":
            solving = input("What are you solving for? > ")
            match solving.lower():
                case "time":
                    while True:
                        try:
                            d = input("Distance? > ")
                            d = float(d)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((vf + vi) / 2) * x - d, x)
                    print(answer)
                case "vi":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            d = input("Distance? > ")
                            d = float(d)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((vf + x) / 2) * t - d, x)
                    print(answer)
                case "vf":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            d = input("Distance? > ")
                            d = float(d)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((x + vi) / 2) * t - d, x)
                    print(answer)
                case "d":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    answer = ((vi + vf) / 2) * t
                    print(f"distance is {answer}")
        case "3":
            solving = input("What are you solving for? > ")
            match solving.lower():
                case "time":
                    while True:
                        try:
                            d = input("Distance? > ")
                            d = float(d)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            a = input("Acceleration? > ")
                            a = float(a)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(vi*x+(1/2*(a*x*2)) - d, x)
                    print(answer)
                case "vi":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            d = input("Distance? > ")
                            d = float(d)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((vf + x) / 2) * t - d, x)
                    print(answer)
                case "acceleration":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            d = input("Distance? > ")
                            d = float(d)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    x = symbols("x")
                    answer = solve(((x + vi) / 2) * t - d, x)
                    print(answer)
                case "d":
                    while True:
                        try:
                            t = input("Time? > ")
                            t = float(t)
                            vi = input("Initial Velocity? > ")
                            vi = float(vi)
                            vf = input("Final Velocity? > ")
                            vf = float(vf)
                            break
                        except ValueError:
                            print("One of the values you entered was not a number")
                    answer = ((vi + vf) / 2) * t
                    print(f"distance is {answer}")
        case "4":
            pass
        case "help":
            print('Equation one is "d=((vf+vi)/2)t" It excludes acceleration\n'
                  'Equation two is "Vf=vi+at" It excludes distance\n'
                  'Equation three is "d=vi*t+½(a*t2)" It excludes final velocity\n'
                  'Equation four is "vf2=vi2+2ad" It excludes time\n')


if __name__ == '__main__':
    while True:
        main()
