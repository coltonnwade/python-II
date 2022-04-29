# Colton Wade Assignment 2
# imports conversion file
import conversion


# Main Function
def main():
    title()
    menu()


    while True:
        choice = input("\nSelect a conversion (a/b): ")  # Gets Input

        # If A is chosen, program will convert feet to meters
        if choice == "a":
            x = float(input("Enter Feet: "))
            a = conversion.feet_to_meters(x)
            total_meters = round(a, 2)
            print("The answer is {0} meters".format(total_meters))
            print("")

        # If B is chosen, program will convert meters to feet
        if choice == "b":
            y = float(input("Enter Meters: "))
            b = conversion.meters_to_feet(y)
            total_feet = round(b, 2)
            print("The answer is {0} meters".format(total_feet))
            print("")

        # Asks user to enter another conversion
        another = input("Would you like to perform another conversion? (y/n): ")

        # If y is chosen, it will display the menu, then start the while loop over.
        if another == "y":
            menu()
            continue

        # If anything but y is chosen, it will end the loop.
        else:
            print("Goodbye!")
            break


# Displays Title/Banner
def title():
    print("Feet and Meters Converter")


# Displays Menu
def menu():
    print("\nConversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")


main()