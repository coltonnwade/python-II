# Colton Wade Lab 7

# Imports Emp
import emp


# Defines Main
def main():

    # Creates Worker Object
    Worker = emp.ProductionWorker()

    # Gets Input and Uses Class Mutators to set Input equal to ProductionWorker Class Attributes
    Name = input("Enter the name: ")
    Worker.set_name(Name)

    ID = input("Enter the ID number: ")
    Worker.set_num(ID)

    ShiftNum = input("Enter the shift number: ")
    Worker.set_shift(ShiftNum)

    HourlyPay = input("Enter the hourly pay rate: ")
    Worker.set_pay(HourlyPay)

    # Prints Worker's Information using Class Accessors
    print("\nProduction Worker Information: ")
    print("Name: " + Worker.get_name())
    print("ID Number: " + Worker.get_num())
    print("Shift: " + Worker.get_shift())
    print("Hourly Pay Rate: " + Worker.get_pay())


main()
