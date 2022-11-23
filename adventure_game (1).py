import time
import random

item = random.choice(["mine", "rpg", "fork", ])


def print_pause(message):
    print(message)
    time.sleep(2)


def play_again():
    again = (input("Would you like to play again? Press"
                   " Y for playing again and N for NO)")).lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        intro()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_house():
    print_pause("You find yourself standing in the entrace of the house")
    print_pause("and you found a magic random box")
    print_pause("you opened the box and found" + " " + item)
    if "mine" in item:
        print_pause("BOOOOOM")
        print_pause("You dead by a mine")
        play_again()
    elif "rpg" in item:
        print_pause("You found an RPG you killed the witch by"
                    " an RPG .. WHOOOAAA")
        play_again()
    else:
        print_pause("You entered the cave and found a"
                    " witch you are dead by her magic")
        play_again()


def play_cave():
    print_pause("You find yourself standing in the entrace of the cave")
    print_pause("and you found a magic random box")
    print_pause("you opened the box and found" + " " + item)
    if "mine" in item:
        print_pause("BOOOOOM")
        print_pause("You dead by a mine")
        play_again()
    elif "rpg" in item:
        print_pause("You found a lion you killed it by an RPG .. WHOOOAAA")
        play_again()
    else:
        print_pause("You entered the cave and found a lion you are dead")
        play_again()


def choosing():
    choice1 = input("Please, enter:\n 1 if you want to go to the"
                    " cave\n 2 if you want to go to the house ")
    if choice1 == "1":
        print_pause("You are walking to the cave")
        play_cave()
    elif choice1 == "2":
        print_pause("You are walking to the house\n")
        play_house()
    else:
        print_pause("please choose a valid number 1 or 2")
        choosing()


def intro():
    print_pause("You find yourself standing in an open field,")
    print_pause("filled with grass and yellow wildflowers.")
    print_pause("You see a small house near the field ...")
    print_pause("and a cave inside the forest")
    print_pause("what you'll choose?")
    choosing()


intro()
# play_cave()
# choosing()
# play_again()
