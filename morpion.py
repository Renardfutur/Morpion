# Créé par Loïc, le 30/10/2020 en Python 3.7

import random
plat=[[".",".","."],[".",".","."],[".",".","."]]
z=0
long=len(plat)
arret=False
num=[0,1,2]
mod=str(input("Jouez-vous contre un ordinateur ou un joueur."))
for i in range(long):
        print(plat[i])


if mod=="joueur":
    while z < 9:
        print("Au tpour du joueur x")
        ligne = int(input("ligne"))
        col = int(input("collone"))
        while plat[ligne - 1][col - 1] != ".":
            if plat[ligne - 1][col - 1] != ".":
                print("Case déja prise")
                ligne = int(input("ligne"))
                col = int(input("collone"))
            else:
                plat[ligne - 1][col - 1] = "x"
        else:
            plat[ligne - 1][col - 1] = "x"
        for i in range(long):
            print(plat[i])
        if plat[0][0] == plat[1][0] == plat[2][0] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][1] == plat[1][1] == plat[2][1] != ".":
            print("Le joueur", plat[0][1], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][2] == plat[2][2] != ".":
            print("Le joueur", plat[0][2], "a gagné")
            arret = True
            break
        elif plat[1][0] == plat[1][1] == plat[1][2] != ".":
            print("Le joueur", plat[1][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[2][1] == plat[2][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[0][1] == plat[0][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[1][1] == plat[2][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][1] == plat[2][0] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[1][1] == plat[0][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        z = z + 1
        if z == 9:
            break
        print("Au tour du joueur o")
        ligne = int(input("ligne"))
        col = int(input("collone"))
        while plat[ligne - 1][col - 1] != ".":
            if plat[ligne - 1][col - 1] != ".":
                print("Case déja prise")
                ligne = int(input("ligne"))
                col = int(input("collone"))
            else:
                plat[ligne - 1][col - 1] = "o"
        else:
            plat[ligne - 1][col - 1] = "o"
        for i in range(long):
            print(plat[i])
        if plat[0][0] == plat[1][0] == plat[2][0] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][1] == plat[1][1] == plat[2][1] != ".":
            print("Le joueur", plat[0][1], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][2] == plat[2][2] != ".":
            print("Le joueur", plat[0][2], "a gagné")
            arret = True
            break
        elif plat[1][0] == plat[1][1] == plat[1][2] != ".":
            print("Le joueur", plat[1][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[2][1] == plat[2][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[0][1] == plat[0][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[1][1] == plat[2][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][1] == plat[2][0] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[1][1] == plat[0][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        if z == 9:
            break
        z = z + 1
    if arret == False:
        print("Match nul")
elif mod=="ordinateur":
    while z < 9:
        print("Au tour du joueur x")
        ligne = int(input("ligne"))
        col = int(input("collone"))
        while plat[ligne - 1][col - 1] != ".":
            if plat[ligne - 1][col - 1] != ".":
                print("Case déja prise")
                ligne = int(input("ligne"))
                col = int(input("collone"))
            else:
                plat[ligne - 1][col - 1] = "x"
        else:
            plat[ligne - 1][col - 1] = "x"
        for i in range(long):
            print(plat[i])
        if plat[0][0] == plat[1][0] == plat[2][0] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][1] == plat[1][1] == plat[2][1] != ".":
            print("Le joueur", plat[0][1], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][2] == plat[2][2] != ".":
            print("Le joueur", plat[0][2], "a gagné")
            arret = True
            break
        elif plat[1][0] == plat[1][1] == plat[1][2] != ".":
            print("Le joueur", plat[1][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[2][1] == plat[2][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[0][1] == plat[0][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[1][1] == plat[2][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][1] == plat[2][0] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[1][1] == plat[0][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        z = z + 1
        if z == 9:
            break
        print("Au tour du joueur o")
        if plat[0][2]==plat[0][1] =="o" and plat[0][1]==".":
            plat[0][0]="o"
        elif plat[0][2]==plat[0][0] =="o" and plat[0][1]==".":
            plat[0][1]="o"
        elif plat[0][1] == plat[0][0] == "o" and plat[0][2]==".":
            plat[0][2]="o"
        elif plat[1][1] == plat[1][2] == "o" and plat[1][0]==".":
            plat[1][0]="o"
        elif plat[1][0] == plat[1][2] == "o" and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[1][1] == plat[1][0] == "o" and plat[1][2]==".":
            plat[1][2]="o"
        elif plat[2][1] == plat[2][2] == "o" and plat[2][0]==".":
            plat[2][0]="o"
        elif plat[2][0] == plat[2][2] == "o" and plat[2][1]==".":
            plat[2][1]="o"
        elif plat[2][1] == plat[2][0] == "o" and plat[2][2]==".":
            plat[2][2]="o"
        elif plat[1][0] == plat[2][0] == "o" and plat[0][0]==".":
            plat[0][0]="o"
        elif plat[0][0] == plat[2][0] == "o" and plat[1][0]==".":
            plat[1][0]="o"
        elif plat[0][0] == plat[1][0] == "o" and plat[2][0]==".":
            plat[2][0]="o"
        elif plat[1][1] == plat[2][1] == "o" and plat[0][1]==".":
            plat[0][1]="o"
        elif plat[0][1] == plat[2][1] == "o" and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[1][1] == plat[0][1] == "o" and plat[2][1]==".":
            plat[2][1]="o"
        elif plat[1][2] == plat[2][2] == "o" and plat[0][2]==".":
            plat[0][2]="o"
        elif plat[0][2] == plat[2][2] == "o" and plat[1][2]==".":
            plat[1][2]="o"
        elif plat[0][2] == plat[1][2] == "o" and plat[2][2]==".":
            plat[2][2]="o"
        elif plat[2][2] == plat[1][1] == "o" and plat[0][0]==".":
            plat[0][0]="o"
        elif plat[0][0] == plat[2][2] == "o" and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[0][0] == plat[1][1] == "o" and plat[2][2]==".":
            plat[2][2]="o"
        elif plat[1][1] == plat[0][2] == "o" and plat[2][0]==".":
            plat[2][0]="o"
        elif plat[2][0] == plat[0][2] == "o" and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[1][1] == plat[2][0] == "o" and plat[0][2]==".":
            plat[0][2]="o"
        elif plat[0][2]==plat[0][1]!="." and plat[0][1]==".":
            plat[0][0]="o"
        elif plat[0][2]==plat[0][0]!="." and plat[0][1]==".":
            plat[0][1]="o"
        elif plat[0][1] == plat[0][0] != "." and plat[0][2]==".":
            plat[0][2]="o"
        elif plat[1][1] == plat[1][2] != "." and plat[1][0]==".":
            plat[1][0]="o"
        elif plat[1][0] == plat[1][2] != "." and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[1][1] == plat[1][0] != "." and plat[1][2]==".":
            plat[1][2]="o"
        elif plat[2][1] == plat[2][2] != "." and plat[2][0]==".":
            plat[2][0]="o"
        elif plat[2][0] == plat[2][2] != "." and plat[2][1]==".":
            plat[2][1]="o"
        elif plat[2][1] == plat[2][0] != "." and plat[2][2]==".":
            plat[2][2]="o"
        elif plat[1][0] == plat[2][0] != "." and plat[0][0]==".":
            plat[0][0]="o"
        elif plat[0][0] == plat[2][0] != "." and plat[1][0]==".":
            plat[1][0]="o"
        elif plat[0][0] == plat[1][0] != "." and plat[2][0]==".":
            plat[2][0]="o"
        elif plat[1][1] == plat[2][1] != "." and plat[0][1]==".":
            plat[0][1]="o"
        elif plat[0][1] == plat[2][1] != "." and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[1][1] == plat[0][1] != "." and plat[2][1]==".":
            plat[2][1]="o"
        elif plat[1][2] == plat[2][2] != "." and plat[0][2]==".":
            plat[0][2]="o"
        elif plat[0][2] == plat[2][2] != "." and plat[1][2]==".":
            plat[1][2]="o"
        elif plat[0][2] == plat[1][2] != "." and plat[2][2]==".":
            plat[2][2]="o"
        elif plat[2][2] == plat[1][1] != "." and plat[0][0]==".":
            plat[0][0]="o"
        elif plat[0][0] == plat[2][2] != "." and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[0][0] == plat[1][1] != "." and plat[2][2]==".":
            plat[2][2]="o"
        elif plat[1][1] == plat[0][2] != "." and plat[2][0]==".":
            plat[2][0]="o"
        elif plat[2][0] == plat[0][2] != "." and plat[1][1]==".":
            plat[1][1]="o"
        elif plat[1][1] == plat[2][0] != "." and plat[0][2]==".":
            plat[0][2]="o"
        else:
            ligne = random.choice(num)
            col = random.choice(num)
            while plat[ligne][col] != ".":
                if plat[ligne][col] != ".":
                    print("Case déja prise")
                    ligne = random.choice(num)
                    col = random.choice(num)
                else:
                    plat[ligne][col] = "o"
            else:
                plat[ligne][col] = "o"
        for i in range(long):
            print(plat[i])
        if plat[0][0] == plat[1][0] == plat[2][0] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][1] == plat[1][1] == plat[2][1] != ".":
            print("Le joueur", plat[0][1], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][2] == plat[2][2] != ".":
            print("Le joueur", plat[0][2], "a gagné")
            arret = True
            break
        elif plat[1][0] == plat[1][1] == plat[1][2] != ".":
            print("Le joueur", plat[1][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[2][1] == plat[2][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[0][1] == plat[0][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][0] == plat[1][1] == plat[2][2] != ".":
            print("Le joueur", plat[0][0], "a gagné")
            arret = True
            break
        elif plat[0][2] == plat[1][1] == plat[2][0] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        elif plat[2][0] == plat[1][1] == plat[0][2] != ".":
            print("Le joueur", plat[2][0], "a gagné")
            arret = True
            break
        if z == 9:
            break
        z=z+1
    if arret == False:
        print("Match nul")