# Colton Wade Assignment 4

def main():

    # While Loop
    while True:

        display_menu()
        # Gets user input choice, to decide which category to display.
        choice = input("Enter your food group choice (1-5): ")

        show_all = read_data()  # sets show_all equal to the result of read_data which is the list of everything
        create_separate_list(show_all, choice)  # Calls Method

        # If choice is greater than 5, or less than 1 it will prompt an error. In order to validate user input is 1-5
        if int(choice) > 5 or int(choice) < 1:
            print("Error! Must pick from menu!\n")
            continue  # Continues until correct choice is made.
        # If user picks 1-5 it will return a formatted list of the appropriate food category
        else:
            # result is equal to what ever create_separate_list returns
            result = create_separate_list(show_all, choice)

            # Header of formatted list
            print("\nName\t\t\t\t\t\tAmount\t\t\tCalories")
            print("-----------------------------------------------------")
            for item in result:
                # This prints a formatted string of the returned list
                # In order to get my list aligned with tabs,
                # I learned you could formatting types and left-aligned everything with < and used character limits
                print("{:<20s}\t\t{:<10s}\t\t{:<10s}".format(item[1], item[2], item[3]))

            # Asks user if they want to perform another conversion
            another_conversion = input("\nWould you like to perform another conversion? (y/n): ")

            # if another_conversion equals "y" then continue through the loop
            if another_conversion == "y":
                continue
            # if another_conversion does not equal "y" then print goodbye and break the loop.
            else:
                print("Goodbye!")
                break


# Displays Menu of Choices
def display_menu():
    print("\nNutrition by Food Group")
    print("1. Dairy")
    print("2. Meat")
    print("3. Vegetables")
    print("4. Fruit")
    print("5. Grains")


# This reads all the data in the file, and stores it in a list called show_all
def read_data():
    file = open("nutrition_data.csv", "r")
    show_all = []
    while True:
        lines = file.readline()
        line = lines.rstrip()
        show_all.append(line.split(","))  # This splits each line in the file by "," and stores it in show_all

        if not lines:
            break

    return show_all


# This groups the show_all list into five different list based on food category
def create_separate_list(show_all, choice):
    # Declares 5 new lists for food categories
    dairy = []
    meat = []
    veggies = []
    fruit = []
    grains = []

    # for each line(item) in show_all it finds the the category in each line then appends it to the appropriate list
    for item in show_all:
        if "Dairy" in item:
            dairy.append(item)
        if "Meat" in item:
            meat.append(item)
        if "Vegetables" in item:
            veggies.append(item)
        if "Fruit" in item:
            fruit.append(item)
        if "Grains" in item:
            grains.append(item)


    # These If statements gets the user inputted choice to return the approrpiate list
    if choice == "1":
        return dairy
    if choice == "2":
        return meat
    if choice == "3":
        return veggies
    if choice == "4":
        return fruit
    if choice == "5":
        return grains


main()