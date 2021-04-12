def main():
    print("Do you need angles? Answer 1 for yes, 0 for no")
    inp = input()
    if inp == "1":
        print("Which one do you want?\n1: Sin\n2: Cos\n3: Tan\n4: All")
        inp = input()
        if inp == "1":
            opp = input("Opp: ")
            opp1, opp2, = opp.split(",")
            opp1 = float(opp1)
            hyp = input("Hyp: ")
            hyp1, hyp2, = hyp.split(",")
            hyp1 = float(hyp1)
            hyp = hyp1
            opp = opp1
            print(f"Sin:\n{opp / hyp}")
        elif inp == "2":
            hyp = input("Hyp: ")
            hyp1, hyp2, = hyp.split(",")
            hyp1 = float(hyp1)
            adj = input("Adj: ")
            adj1, adj2, = adj.split(",")
            adj1 = float(adj1)
            adj = adj1
            hyp = hyp1
            print(f"Cos:\n{adj / hyp}")
        elif inp == "3":
            opp = input("Opp: ")
            opp1, opp2, = opp.split(",")
            opp1 = float(opp1)
            adj = input("Adj: ")
            adj1, adj2, = adj.split(",")
            adj1 = float(adj1)
            opp = opp1
            adj = adj1
            print(f"Tan:\n{opp / adj}")
        elif inp == "4":
            opp = input("Opp: ")
            opp1, opp2, = opp.split(",")
            opp1 = float(opp1)
            adj = input("Adj: ")
            adj1, adj2, = adj.split(",")
            adj1 = float(adj1)
            hyp = input("Hyp: ")
            hyp1, hyp2, = hyp.split(",")
            hyp1 = float(hyp1)
            opp = opp1
            adj = adj1
            hyp = hyp1

            print(f"Sin:\n{opp / hyp}")
            print(f"Cos:\n{adj / hyp}")
            print(f"Tan:\n{opp / adj}")
    else:
        print("Which one do you want?\n1: Sin\n2: Cos\n3: Tan\n4: All")
        inp = input()
        if inp == "1":
            opp = float(input("Opp: "))
            hyp = float(input("Hyp: "))
            print(f"Sin:\n{opp/hyp}")
        elif inp == "2":
            hyp = float(input("Hyp: "))
            adj = float(input("Adj: "))
            print(f"Cos:\n{adj / hyp}")
        elif inp == "3":
            opp = float(input("Opp: "))
            adj = float(input("Adj: "))
            print(f"Tan:\n{opp / adj}")
        elif inp == "4":
            opp = float(input("Opp: "))
            adj = float(input("Adj: "))
            hyp = float(input("Hyp: "))
            print(f"Sin:\n{opp / hyp}")
            print(f"Cos:\n{adj / hyp}")
            print(f"Tan:\n{opp / adj}")


while True:
    main()
