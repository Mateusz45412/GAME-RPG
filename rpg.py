import name_module
nick = (name_module.sex())
energy = 100
gold = 100
equipment = {'sword': 15, 'axe': 50, 'stock': 2}
snake = 90
eat = 10

print("Welcome to game RPG")
print(f"Welcome {nick} !")

while (energy>=0):
    print(f"gold = {gold}\nenergy = {energy}")
    print(f"{nick} choose a place")
    place = input("inn(i), forest(f)").lower()
    if place == "i":
        print(f"{nick} you are in the inn, you are talking:")
        print("1-poszukuje pracy")
        print("2-chce się napić piwa")
        do = int(input("wpisz opcje którą wybierasz 1 lub 2 "))
        if do == 1:
            print("OK pozmywaj naczynia a dostaniesz  10 gramów złota")
            deal = input("do you agree y/n").lower()
            if deal == "y":
                w = True
                while w == True:
                    wash = input("enter 3 x washing")
                    w = (wash != ("washing" * 3))
                print("washing\n" * 30, "congratulations you have 10 grams of gold")
                energy = energy-1
                gold = gold+10
            elif deal == "n":
                print("Trudno twoja sprawa")
        elif do == 2:
                print("Beer costs 10 grams of gold")
                deal = input("do you agree y/n").lower()
                if deal == "y":
                    print("drink\n" * 30, "Good Beer")
                    energy = energy+1
                    gold = gold-10
                elif deal == "n":
                    print("no it's not")

    if place == "f":
        print(f"{nick} you meet a snake in the forest, what do you do? :")
        print("1-FLIGH")
        print("2-ESCAPE")
        do = int(input("what you choose 1 or 2 "))
        if do == 1:
            while snake != 0:
                print(equipment)
                item = input("enter what you want to attack ").lower()
                print("Attack" * 5)
                snake = snake - equipment[item]
                energy = energy - 2
                eat = eat + 10
                print(f"snake - {snake}\nyou energy {energy}")
                if snake <= 0:
                    print(f"YOU ARE WON snake is dead\nsnake {snake}\nyou energy {energy}")
                    break
        elif do == 2:
            print("the snake is faster, you are bitten, you get - 3 pts")
            energy = energy-3
print("GAME OVER ENERGY = 0")