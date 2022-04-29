# Colton Wade Lab 8

# Create Class

class Pet:

    # __init__ method that defines data attributes
    def __init__(self, __name="None", __animal_type="None", __age="None"):
        self.__name = __name
        self.__animal_type = __animal_type
        self.__age = __age

    # Class Mutators
    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    # Class Accessors
    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


myPet = Pet()

pet_name = input("Enter the Pet's Name: ")
myPet.set_name(pet_name)

pet_at = input("Enter the Animal Type: ")
myPet.set_animal_type(pet_at)

pet_age = input("Enter the Pet's Age: ")
myPet.set_age(pet_age)

print("Pet Name: {0}  Pet Type: {1}  Pet Age: {2}\n".format(myPet.get_name(), myPet.get_animal_type(), myPet.get_age()))











