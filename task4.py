import colorama
from colorama import Fore
from random import randint

name = input("Enter your name: ")

pc = 0
user = 0
count = 0

while True:
    count += 1
    input("Your turn press Enter")
    rand1 = randint(1, 6)
    rand2 = randint(1, 6)
    if rand1 == rand2:
        user += 2
        print("Congratulations!")
    result = rand1 + rand2
    print("Your throw", + rand1, "and", rand2)
    input("PC won't throw a number Press Enter")
    pcrand1 = randint(1, 6) 
    pcrand2 = randint(1, 6)
    if pcrand1 == pcrand2:
        pc += 2
        print("Congratulation!")
    result_pc = pcrand1 + pcrand2
    print("PC throw", pcrand1, "and", pcrand2)


    if result > result_pc:
        user += 1
    elif result < result_pc:
        pc += 1
    if pc == 10 or user == 10:
        break

if pc < user:
    print("The winner is", name,  "with", user,  "points")
else:
    print("Winner is PC with ",  pc,  Fore.GREEN + "points!")                