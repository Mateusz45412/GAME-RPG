import random

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')

girl = 'girl.txt'
with open(girl, 'r', encoding = "utf-8") as g:
    girls = (g.readline()).split(',')

boy = 'boy.txt'
with open (boy, 'r', encoding = "utf-8") as b:
    boy = (b.readline()).split(',')

gender = input("enter the gender of the player (W/M) ").lower()
breed = ["BLACK", "WHITE"]
def sex():
    if gender == "w":
        nam = random.choice(girls)
    elif gender == "m":
        nam = random.choice(boy)
    return nam
def bree():
        return random.choice(breed)
