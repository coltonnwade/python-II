# Colton Wade
# Assignment 10

# Person Class
class Person:
    def __init__(self, fName="", lName="", Email=""):
        self.fName = fName
        self.lName = lName
        self.Email = Email

    # getInformation Method
    def getInformation(self):
        pass


# Customer Class Inherited from Person
class Customer(Person):

    # Overrides Person's __init__ method and adds Customer Number
    def __init__(self, fName="", lName="", Email="", Num=""):
        super().__init__(fName, lName, Email)
        self.Num = Num

    # Overrides Person's getInformation method
    def getInformation(self):
        print(f"Customer: {self.fName} {self.lName}")
        print("Customer Email: " + self.Email)
        print("Customer Number: " + self.Num)


# Employee Class Inherited from Person
class Employee(Person):

    # Overrides Person's __init__ method and adds Employee SSN
    def __init__(self, fName="", lName="", Email="", SSN=""):
        super().__init__(fName, lName, Email)
        self.SSN = SSN

    # Overrides Person's getInformation method
    def getInformation(self):
        print(f"Customer: {self.fName} {self.lName}")
        print("Employee Email : " + self.Email)
        print("Employee SSN: " + self.SSN)


# Display Method
def display(obj):

    # Uses isinstance to tell if obj belongs to the Customer or Employee Class
    # Once determined, it will then print Customer or Employee Information then call the getInformation() method
    if isinstance(obj, Customer):
        print("\nCUSTOMER INFORMATION:")
        obj.getInformation()
    if isinstance(obj, Employee):
        print("\nEMPLOYEE INFORMATION:")
        obj.getInformation()


# Main Method
def main():

    # Header
    print("Customer/Employee Data Entry")

    # While Loop
    while True:
        print("")
        # Gets Input for Basic Person Class
        FirstName = input("First Name: ")
        LastName = input("Last Name: ")
        Email = input("Email: ")

        # Asks User if Person is Customer or Employee
        Type = input("Customer or Employee? (c/e): ")

        # Validates Type with While Loop to keep the program running
        # While Type does not equal c or e, it will print an error and ask the user to choose again.
        while Type != "c" and Type != "e":
            print("Must pick Employee(e) or Customer(c)!")
            Type = input("Customer or Employee? (c/e): ")
            # if Type is equal to c or e it will break out of the loop
            if Type == "c" or Type == "e":
                break

        # If user chooses "c" it will ask user to enter the Customer Number
        if Type == "c":
            Number = input("\nNumber: ")
            obj = Customer(FirstName, LastName, Email, Number)  # Creates Customer Object with Inputted Data
            display(obj)  # Sends obj to display() method

        # If user chooses "e" it will ask the user to enter Employee SSN
        if Type == "e":
            SSN = input("\nSSN: ")
            obj = Employee(FirstName, LastName, Email, SSN)  # Creates Employee Object with Inputted Data
            display(obj)  # sends obj to display() method

        # Asks user if they would like to continue
        choice = input("\nContinue? (y/n): ")
        # If user chooses "y" then it will continue
        if choice == "y":
            continue
        # If user doesn't choose "y" then it will print Goodbye! and break the loop ending the program
        else:
            print("Goodbye!")
            break

# Calls Main
main()