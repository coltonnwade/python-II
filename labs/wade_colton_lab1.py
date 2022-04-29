# Colton Wade Lab 1

# Set values of x and y for While Loop
x = 1
y = 0


print("Table of Powers\n")
# While X is Greater than Y, Program will ask you to input integers
while x > y:

    # Input gets your Starting and End Value for your table
    x = int(input("Enter a Starting Number: "))
    y = int(input("Enter a Stop Number: "))

    # If X is greater than or equal to Y, it will give you a warning.
    if x >= y:
        print("Starting Number must be Greater than Stop Number!\n")

    # If x is less than Y, the program will print the Table of Powers.
    if x <= y:
        print("\nNumber\t\tSquared\t\tCubed")
        print("======\t\t======\t\t======")

        # Prints Starting to End Number, and their Squared and Cubed values
        for z in range(x,y+1):
            print("{0}\t\t{1}\t\t{2}".format(z, z**2, z**3))
            
