#TASK1
# Create a class named Car that has the following attributes: make, model, and year. It should also have a method called
# get_info() that returns a string with the car's make, model, and year.
#
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#        return str(self.make) + " "+ str(self.model) + " "+ str(self.year)
#
# car1=Car("Ford", "Focus", 2010)
# car2=Car("Ford", "Mustang", 2020)
# car3=Car("Vw", "Beatle", 2022)
#
# print(car1.get_info())
# print(car2.get_info())
# print(car3.get_info())

#TASK2
# Create a class named Rectangle that has the following attributes: width and height. It should also have methods
# called area() and perimeter() that return the area and perimeter of the rectangle, respectively.
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return (self.width*2)+(self.height*2)
#
# rect1= Rectangle (4,6)
# rect2= Rectangle (3,5)
#
# print(f'The area of Rectangle 1 is {rect1.area()}')
# print(f'The perimeter of Rectangle 2 is {rect2.perimeter()}')

#TASK3
# Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name.
# It should also have methods called deposit() and withdraw() that update the balance accordingly.

# class BankAccount:
#     def __init__(self, account_number, balance, owner_name):
#         self.account_number = account_number
#         self.balance = balance
#         self.owner_name = owner_name
#
#     def deposit(self):
#         income = input("Enter the amount of the deposit: ")
#         new_balance = self.balance + int(income)
#         return new_balance
#
#     def withdraw(self):
#         deduction = input("Enter the amount of the withdrawal: ")
#         new_balance = self.balance - int(deduction)
#         return new_balance
#
# BankAcc1=BankAccount("LT12345", 100, "Inga")
# BankAcc2=BankAccount("LT64758", 300, "Jen")
#
# print(f'Current balance in your Bank account is: {BankAcc1.deposit()}')
# print(f'Current balance in your Bank account is: {BankAcc2.withdraw()}')

#TASK4
# Create a class named Person that has the following attributes: name, age, and address. It should also have a method
# called get_info() that returns a string with the person's name, age, and address.
#
# class Person:
#     def __init__(self, name, age, address ):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def get_info(self):
#         return f'Persons name is {self.name}, she is {self.age} years old and lives in {self.address}'
#
# pers1=Person("Inga", 22, "Vilnius")
# pers2=Person("Jen", 66, "Kaunas")
#
# print(pers1.get_info())
# print(pers2.get_info())

#TASK5
# Create a class named Animal that has the following attributes: name and species. It should also have a method called
# speak() that returns a string with the animal's sound.

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def speak(self, sound):
#         return f'The sound of the animal {self.name} is {sound}'
#
# Anim1=Animal("Dog", "Labrador")
# Anim2=Animal("Cat", "Bombay")
#
# print(Anim1.speak("au au"))
# print(Anim2.speak("miau miau"))

#TASK6
# Create a base class named Vehicle that has the following attributes: make, model, and year. It should also have a
# method called get_info() that returns a string with the vehicle's make, model, and year. Then create two subclasses,
# Car and Truck, that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle

# class Vehicle():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_info(self):
#        return str(self.make) + " "+ str(self.model) + " "+ str(self.year)
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, type):
#         super().__init__(make, model, year)
#         self.type = type
#
#     def get_info_car(self):
#        return "The car is: " + str(self.make) + " "+ str(self.model) + " "+ str(self.year) +" " + str(self.type)
#
# class Truck(Vehicle):
#     def __init__(self, make, model, year, power):
#         super().__init__(make, model, year)
#         self.power = power
#
#     def get_info_truck(self):
#        return "The truck is: " + str(self.make) + " "+ str(self.model) + " "+ str(self.year) +" with power " + str(self.power)
#
# car1=Car("Ford", "Mustang", 2010, "convertible")
# truck1=Truck("Dodge", "Ram", 2020, 400)
#
# print(car1.get_info_car())
# print(truck1.get_info_truck())

#TASK7
# Create a base class named Person that has the following attributes: name, age, and address. It should also have a
# method called get_info() that returns a string with the person's name, age, and address. ' \
# Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes
# and methods specific to each role.

class Person:
    def __init__(self, name, age, address ):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f'Persons name is {self.name}, she is {self.age} years old and lives in {self.address}'

class Student(Person):
    def __init__(self, name, age, address, grade, program):
        super().__init__(name, age, address)
        self.grade = grade
        self.program = program

    def student_info(self):
        return f'Student {self.name} is in {self.grade} grade and studies {self.program}'

class Teacher(Person):
    def __init__(self, name, age, address, degree, subject):
        super().__init__(name, age, address)
        self.degree = degree
        self.subject = subject

    def teacher_info(self):
        return f'Teacher {self.name} has a {self.degree} degree and teaches {self.subject}'

stud1=Student("Inga", 22, "Vilnius", 3, "Economics")
teach1=Teacher("Aldona", 53, "Vilnius", "Professor", "Biology")

print(stud1.student_info())
print(teach1.teacher_info())