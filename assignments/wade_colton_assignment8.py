# Colton Wade Assignment 8
import emp


# Main Method
def main():

    # Creates Three Employees
    Emp1 = emp.Employee("Susan Meyers", 47899, "Accounting", "Vice President")
    Emp2 = emp.Employee("Mark Jones", 39119, "IT", "Programmer")
    Emp3 = emp.Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

    # Prints employees out as a table format
    print("Name\t\t\t\tID Number\t\tDepartment\t\t\tJob Title")
    print("{0:<15}\t\t{1:<10}\t\t{2:<15}\t\t{3:<15}\t\t".format(Emp1.name, Emp1.IDNum, Emp1.Department, Emp1.Title))
    print("{0:<15}\t\t{1:<10}\t\t{2:<15}\t\t{3:<15}\t\t".format(Emp2.name, Emp2.IDNum, Emp2.Department, Emp2.Title))
    print("{0:<15}\t\t{1:<10}\t\t{2:<15}\t\t{3:<15}\t\t".format(Emp3.name, Emp3.IDNum, Emp3.Department, Emp3.Title))

    # Prints Each Employee's Data
    print("\nEmployee 1: ")
    print(Emp1)

    print("\nEmployee 2:")
    print(Emp2)

    print("\nEmployee 3:")
    print(Emp3)


main()
