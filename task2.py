import colorama
from colorama import Fore
colorama.init()

day = int(input("Enter day: "))
month = int(input("Enter month: "))

def date(day, month):
    if day == 1 and month == 1:
        print(Fore.GREEN + "Happy New Year!!!")
    elif day == 7 and month == 1:
        print(Fore.GREEN + "Merry Christmas!!!")
    elif day == 19 and month == 1:
        print(Fore.GREEN + "Epiphany!")
    elif day == 8 and month == 3:
        print(Fore.GREEN + "International Women's Day!")
    elif day == 9 and month == 5:
        print(Fore.GREEN + "Day of Victory!")
    else:
        print(Fore.RED + "Wrong date(((")        


date(day, month)        
