# Colton Wade Lab 11

# print_lines method
def print_lines(n):
    # Base Case
    if n == 0:
        return

    # Calls method again
    print_lines(n - 1)
    # For loop to print *'s from 1 to nth entered
    for i in range(n):
        print("*", end=" ")
    print()  # New Line


# Main Method
def main():
    # Asks user for input and calls print_lines
    n = int(input("How many lines to display?: "))
    print_lines(n)


main()
