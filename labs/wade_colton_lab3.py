# Colton Wade Lab 3

try:
    # Opens File and Reads Line
    file = open("mod3numlist.txt", "r")
    line = file.readline()

    # Creates a list for even and odd
    even = ""
    odd = ""

    # Reads each line in file and tests if it is even and odd
    for line in file:
        if (int(line) % 2) == 0:
            even += line  # Appends Line to list Even
        else:
            odd += line  # Appends Line to list odd
    file.close()  # Closes File
    print(list, "\n")

    # Opens even.txt file and writes the list even to the file
    even_file = open("even.txt", "w")
    even_file.write(even)
    even_file.write("\n")
    even_file.close()

    # Opens the odd.txt file and writes the list to the file
    odd_file = open("odd.txt", "w")
    odd_file.write(odd)
    odd_file.write("\n")
    odd_file.close()


# When opening the file, if it is not found it will print "File not found"
except FileNotFoundError:
    print("File not found")


