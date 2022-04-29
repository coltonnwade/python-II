# Colton Wade Assignment 9

# Imports emp
import emp


def main():

    # Creates Shift Supervisor
    Supervisor = emp.ShiftSupervisor()

    Name = input("Enter the name: ")
    Supervisor.set_name(Name)

    ID = input("Enter the ID number: ")
    Supervisor.set_num(ID)

    Salary = input("Enter the annual salary: ")
    Supervisor.set_salary(Salary)

    Bonus = input("Enter the bonus: ")
    Supervisor.set_bonus(Bonus)

    print(Supervisor)


main()






