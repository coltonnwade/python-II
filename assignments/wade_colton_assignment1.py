# Colton Wade Assignment 1

# COST OF ITEMS SHIPPING COST
# =============================
# < 30.00         $5.95
# 30.00-49.99     $7.95
# 50.00-74.99     $9.95
# > 75.00         FREE


print("======================================")
print("Shipping Calcualtor")

# While Loop
while True:

    print("======================================")
    print("")
    # Gets Input for Cost Of Item
    x = float(input("Enter cost of items ordered: "))

    # If X is Less than 0, an error will pop up, and ask you to try again.
    if x < 0:
        print("You must enter a positive number. Please Try Again")
        continue

    # If x is Less than 30
    if x < 30.00:
        print("")
        y = 5.95
        print("Shipping Cost: {0}".format(y))
        print("Total Cost {0} ".format(x+5.95))
        c = input("Continue? (y/n): ")

        # Continue
        if c == "y":
            continue
        # if input doesn't = y then it quits the program
        else:
            print("======================================")
            print("Bye")
            break

    # If X is in between 30 and 49.99
    elif 30.00 <= x <= 49.99:
        print("")
        y = 7.95
        print("Shipping Cost: {0}".format(y))
        total_cost = x + y
        z = '{0:.2f}'.format(total_cost)  # Formats total cost into two decimal places.
        print("Total Cost:", z)
        c = input("Continue? (y/n): ")

        # Continue
        if c == "y":
            continue
            print("")
            x = input("Enter cost of items ordered: ")
        else:
            print("======================================")
            print("Bye")
            break

    # If x is in between 50 and 74.99
    elif 50.00 <= x <= 74.99:
        print("")
        y = 9.95
        print("Shipping Cost: {0}".format(y))
        cost = x + y
        total_cost = round(cost, 2)  # Rounds total cost into two decimal places.
        print("Total Cost:", total_cost)
        c = input("Continue? (y/n): ")

        # Continue
        if c == "y":
            continue
            print("")
            x = input("Enter cost of items ordered: ")
        else:
            print("======================================")
            print("Bye")
            break

    # If x is greater or equal to 75
    elif x >= 75.00:
        print("")
        y = "FREE"
        print("Shipping Cost: {0}".format(y))
        print("Total Cost {0} ".format(x))
        c = input("Continue? (y/n): ")

        # Continue
        if c == "y":
            continue
            print("")
            x = input("Enter cost of items ordered: ")

        else:
            print("======================================")
            print("Bye")
            break

