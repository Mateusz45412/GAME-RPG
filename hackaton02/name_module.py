import random
girl = 'girl.txt'
with open(girl, 'r', encoding = "utf-8") as g:
    girls = (g.readline()).split(',')

boy = 'boy.txt'
with open (boy, 'r', encoding = "utf-8") as b:
    boy = (b.readline()).split(',')
gender = "g"
while gender != "w" and gender != "m" :
    gender = input("enter the gender of the player (W💃/M🕺) ").lower()
    if gender != "w" and gender != "m":
        print("Type correctly 'w' or 'm'")

breed = ["BLACK", "WHITE"]
def sex():
    if gender == "w":
        nam = random.choice(girls)
    elif gender == "m":
        nam = random.choice(boy)
    return nam

def bree():
    return random.choice(breed)
