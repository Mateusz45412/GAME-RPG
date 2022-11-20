import name_module
import energy_module
nick = (name_module.sex())
start_energy = 100
energy = 100
gold = 100
equipment = {'sword': 15, 'axe': 50, 'stock': 2}
snake_start = 90
snake_energy = 90
eat = 10
print(f"Welcome {nick} !")
while (energy>=0):
    energy_module.energies(energy, start_energy, nick)
    print(f"gold = {gold}")
    print(f"{nick} choose a place")
    place = input("inn(i), forest(f)").lower()
    if place == "i":
        print(f"{nick} you are in the inn, you are talking:")
        print("1- I looking for a job")
        print("2- I wants to drink beer")
        do = int(input("choose 1 or 2 "))
        if do == 1:
            print("OK wash the dishes a 10 grams of gold")
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
                print("your business")
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
        print("1-ATTACK")
        print("2-ESCAPE")
        do = int(input("what you choose 1 or 2 "))
        if do == 1:
            while snake_energy != 0:
                print(equipment)
                try:
                    item = input("enter what you want to attack ").lower()
                    print("Attack" * 5)
                    snake_energy = snake_energy - equipment[item]
                    energy = energy - 5
                    eat = eat + 10
                    energy_module.energies(snake_energy, snake_start, "SNAKE")
                    energy_module.energies(energy, start_energy, nick)
                except KeyError:
                    print("Type correctly item")
                if snake_energy <= 0:
                    print(f"YOU ARE WON snake is dead")
                    energy_module.energies(snake_energy, snake_start, "SNAKE")
                    break
        elif do == 2:
            print("the snake is faster, you are bitten, you get - 3 pts")
            energy = energy-7
            energy_module.energies(energy, start_energy, nick)
            energy_module.energies(snake_energy, snake_start, "SNAKE")
print("GAME OVER ENERGY = 0")