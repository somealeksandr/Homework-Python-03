import colorama
from colorama import Fore, Back, Style
colorama.init()

distance = int(input("Enter distance: "))

fuel = int(input("Fuel consumption per 100 km: "))

def results(distance, fuel):
    result = round(distance / 50 * fuel, 2)
    print("Your car consumption " + Fore.GREEN + str(result) + Fore.RESET + " l. fuel is both ways")

results(distance, fuel)    