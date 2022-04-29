# Colton Wade
# Lab 10

# SimpleCounter Class
class SimpleCounter:
    def __init__(self, firstNum):
        self._count = firstNum

    # Increments by adding 1 to count
    def increment(self):
        self._count += 1

    # Sets count to 0
    def clear(self):
        self._count = 0

    # Returns value
    def get_value(self):
        return self._count

    # Does Nothing, method is null
    def decrement(self):
        pass


# AdvancedCounter Class
class AdvancedCounter(SimpleCounter):

    # Inherits SimpleCounter's __init__ method
    def __init__(self, firstNum):
        SimpleCounter.__init__(self, firstNum)

    # Overrides increment to add 2 to count instead of 1
    def increment(self):
        self._count += 2

    # Overrides Decrement by subtracting 1 from count
    def decrement(self):
        self._count -= 1


# Main Method
def main():
    # Asks User for Initial Number
    Input = int(input("Add an initial number: "))

    # Instantiates Simple and Advanced Counter Objects
    SC = SimpleCounter(Input)
    AC = AdvancedCounter(Input)

    # Increment
    print("\nIncrementing...")

    # Increments both SC and AC
    SC.increment()
    AC.increment()

    # Gets and Prints Value of SC and AC using get_value() methods
    result = SC.get_value()
    print(result)
    result = AC.get_value()
    print(result)

    # Decrement
    print("\nDecrementing...")

    # Decrements both SC and AC
    SC.decrement()
    AC.decrement()

    # Gets and Prints Value of SC and AC using get_value() methods
    result = SC.get_value()
    print(result)
    result = AC.get_value()
    print(result)

    # Clear
    print("\nClearing...")
    # Clears both SC and AC
    SC.clear()
    AC.clear()

    # Gets and Prints Value of SC and AC using get_value() methods
    result = SC.get_value()
    print(result)
    result = AC.get_value()
    print(result)


# Calls Main
main()