import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print("Guess The Number: Python Edition")
print()

scoreboard = 0
loses = 0
times = 3
print("Starting..")
print()

Game = True
while Game == True:

    def GameEnd():
            global times, scoreboard, Game, calc, loses, ask
            if (scoreboard == times) or (loses == times):
                ask = print('Wanna Continue?' + Fore.RED + ' y/n: ')
                ask = input()
                ask.lower
                if (ask == "y"):
                    times = times + 3
                    return True, times
                elif ask == "n":
                    print("scoreboard:" + Fore.GREEN + str(scoreboard))
                    print("loses:"+ Fore.RED + str(loses))
                    input("Press Enter to close...")
                    Game = False
                    return Game
                elif ask != "n" or ask != "y":
                    print ("Not recognizable input..")
                    input("Press Enter to close...")
                    Game = False
                    return Game
            else:
                return Game
    
    scoreboard = int(scoreboard)
    loses = int(loses)
    poggers = random.randint(1, 5)
    guess = input("Guess the number: (1 - 5) ")
    guess = int(guess)
    if (guess == poggers):
        print ("You've Won!")
        scoreboard+=1
        GameEnd() 

    elif(guess != poggers):
        print ("no luck")
        loses+=1
        if (guess > poggers and poggers < 6):
            calc = poggers - guess
            print("You were close by " + str(calc))
            GameEnd()
    
        elif(guess < poggers and poggers < 6):
            calc = poggers - guess
            print("You were close by " + str(calc))
            GameEnd()

        

    else:
        break
