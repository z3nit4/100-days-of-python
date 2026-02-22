
# OBJECT-ORIENTED PROGRAMMING

"""
OOP is a prgoramming paradigm that tries to model the real world into the programming world.
We take real world objects and try to make abstract models of them in the programming world: 
People, cities, books, buildings etc. We wanna make abstract models of them. 
To do that we use classes and objects. 
"""

"""
What is a Class?

A class is like a blueprint or template for creating objects. 
- Think of it as a "cookie cutter."
- It defines attributes (data) and methods (functions) that the objects made from it will have.
"""

# How to define a class:

class Person:
    """
    How do we create objects of a class?
    We do that by calling a constructor. 
    A constructor is a method in our class that we need to call whenever we want to creat a object. 
    """
    def __init__(self, name, age): # self is a parameter that has to be in every method. It refers to the object we're dealing with rn. 
        self.name = name
        self.age = age

    def talk(self):
        print(f"{self.name} says Hello World!")

    def __del__ (self):
        print("Object deleted")
 

# Person -> class
# __init__ -> special constructor method called when a new Person is created
# self -> refers to the instance (object) itself

"""
What is an Object?

An object is an instance of a class.
"""

person1 = Person("Zeen", 22) # Create an object
person1.talk() # Output: Zeen says Hellow World!
print(person1.age) # Ouput: 22

# person1 -> object
# Can create multiple objects from the same class:

person2 = Person("Xen", 88)
person2.talk() # Output: Xen says Hello World! 

# del person1 # To delete the object

"""
Attributes vs Methods

Attributes = properties of the object (like name, age)
Methods = actions/functions the object can do (like talk)
"""

# print(person2.name) # Attribute
# person1.talk() # Method

"""
Why Use Classes?

- Organizes code better than just functions
- Makes it easy to reuse and scale
- Essential for OOP
"""

class Dog:
    def __init__(self, name, age):  # Constructor method
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def __str__(self):
        return "Name: {}, Age: {}".format(self.name, self.age)

my_dog = Dog("Rex", 3)  
my_dog.bark()           
print(my_dog.age)        

dog2 = Dog("Bella", 5)
dog2.bark()

print(dog2)

