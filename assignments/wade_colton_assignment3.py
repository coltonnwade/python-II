# Colton Wade Assignment 3

# Main
def main():

    # While loop to open file
    while True:
        try:

            contact_file = input("Enter Contacts File Name: ")
            open(contact_file, "r")
            break

        except FileNotFoundError:
            print("File Does Not Exist! Please Try Again")

    # While Loop to show menu, and enter commands
    while True:
        menu()
        choice = input("Enter Command: ")
        print("")

        if choice == "view":
            view_contacts(contact_file)
        if choice == "add":
            add_contacts(contact_file)
        if choice == "del":
            delete_contacts(contact_file)
        if choice == "exit":
            print("Goodbye!")
            break


# Menu
def menu():
    print("")
    print("====COMMAND MENU====")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")


# View Contacts
def view_contacts(contact_file):

    # Loops through file and prints the contacts
    file = open(contact_file, "r")
    while True:
        lines = file.readlines()
        count = 0  # Initializes a Count
        for line in lines:
            count += 1  # Adds 1 to Count for every line
            print("{0}. {1}".format(count, line.rstrip("\n")))  # Prints the number of the line, and the contact.


        if not lines:
            break


# Adds Contact
def add_contacts(contact_file):

    # Gets Name, Email, and Phone #
    name = str(input("Name: "))
    email = str(input("Email: "))
    phone = str(input("Phone: "))

    # Opens the file in append mode, and formats the name, email, and phone # into a string called new_contact
    add = open(contact_file, "a")
    new_contact = (name + ", " + email + ", " + phone)
    add.write(new_contact)  # Appends the new_contact to the new line in the file
    add.write("\n")
    add.close()

    print("{0} has been added!".format(name))


# Delete Contacts
def delete_contacts(contact_file):

    # Shows the contacts,
    view_contacts(contact_file)
    contact = input("Enter the Number of the Contact to Delete: ")
    c = int(contact)  # Stores the input as an integer

    file = open(contact_file, "r")
    lines = file.readlines()

    while True:
        count = 0
        contacts = ""

        # Loops through lines and gets their line #
        for line in lines:
            count += 1
            if count == c:  # Skip's over the contact you want to delete
                pass
            else:
                contacts += line  # Writes the rest of the contacts to a string named contacts
        file.close()

        # Writes the string contacts, to the file
        write_file = open(contact_file, "w")
        write_file.write(contacts[:-1])
        write_file.write("\n")
        write_file.close()
        print("{0} has been deleted!".format(c))
        break


main()