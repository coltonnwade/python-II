# Colton Wade Assignment 11

print("Greatest Common Divisor\n")  # Title


# Greatest Common Divisor Function
def gcd(x, y):
    r = x % y  # r equals remainder of x divided by y

    if r == 0:  # if r is equal to 0 it will return y
        return y
    else:  # if r is not equal to 0 it will call its self until r = 0
        return gcd(y, r)


# Continue Method
def Continue():
    choice = input("Continue(y/n): ")

    if choice != "y" and choice != "n":  # If user does input 'y' or 'n' then print error message and call Continue()
        print("ERROR: Must Pick 'y' Or 'n'")
        Continue()

    if choice == "y":  # If user picks y then call main
        main()
    if choice == "n":  # If user picks n then print Goodbye! and end program
        print()
        print("Goodbye!")


# Main Function
def main():
    # Try/Except to validate user input
    try:
        # Gets User Input for First Number x and Second Number y
        x = int(input("Enter First Number: "))
        y = int(input("Enter Second Number: "))

        # If x is greater than y
        if x > y:
            print(f"Greatest Common Divisor: {gcd(x, y)}\n")   # Prints Result of GCD
            Continue()  # Calls Continue()

        # If x is less than y
        else:
            print("ERROR: First Number Must Be Greater Than Second Number!")
            main()  # Calls Main()

    # If user enters non int it will print error message and call main again
    except ValueError:
        print("ERROR: Must Enter Number!")
        main()


main()