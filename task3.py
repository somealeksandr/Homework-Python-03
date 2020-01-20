import colorama
from colorama import Fore

colorama.init()

distance = int(input("Enter distance in meter: "))
time = int(input("Enter time in second: "))

def speed(distance, time):
    result = distance / time
    return round(result, 2)

result = speed(distance, time)
print("Speed = " + Fore.GREEN + str(result))
