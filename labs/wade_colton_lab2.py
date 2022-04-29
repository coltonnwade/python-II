# Colton Wade Lab 2
import random


def main():

    title()
    x = input("Roll the dice?(y/n): ")
    if x == "y":
        roll_dice()
        while True:  # This Loops through and asks if you want to roll the dice again, until you answer no.
            print("")
            y = input("Roll again?(y/n): ")
            if y == "y":
                roll_dice()
            else:
                print("Goodbye!")
                break

    else:
        print("Goodbye!")


# Function Prints Title
def title():
    print("\n==Dice Roller==")


# Function Rolls a "Dice" chooses a number 1-6 then returns the value.
def roll():
    value = random.randint(1, 6)
    return value


# This function calls roll() twice, then stores the value in "dice1 & dice2" then adds the total, and prints it.
def roll_dice():
    dice1 = roll()
    dice2 = roll()
    total = dice1 + dice2
    print("Die 1:", dice1)
    print("Die 2:", dice2)
    print("Total:", total)
    combos(total, dice1, dice2)


# This function tests for special combinations
def combos(total, dice1, dice2):
    if total == 2:
        print("Snake Eyes!")
    if total == 12:
        print("Boxcars!")
    if dice1 == 2 and dice2 == 2:
        print("Ballerina!")
    if dice1 == 4 and dice2 == 4:
        print("Square Pair!")
    if dice1 == 4 and dice2 == 5:
        print("Tennessee!")


main()
