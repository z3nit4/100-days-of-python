# INHERITANCE

# Inheritance lets one class reuse another class’s code. Remember, a class is like a blueprint or template for creating objects.

# Parent class would be Animal, Child classes are the various Animals (Dogs, Cats etc.)
# Instead of rewriting everything for each class again… You inherit it.

class Animal:
    def __init__(self, species, name, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age

    def __str__(self):
        return f"{self.name}. species name: {self.species}, is {self.diet} and has a lifespan of {self.age} years."

class Dog(Animal):
    def bark(self):
        print("\nWoof")

    def breed(self, name):
        print(f"Breed name {name}")

my_dog = Dog("Canus lupus familiaris", "Dog", "Carnivorous", 12)

my_dog.bark()
my_dog.breed("Maltese")
print(my_dog)


class Cat(Animal):
    def meow(self):
        print("\nMeow")
    
    def breed(self, name):
        print(f"Breed name: {name}")

my_cat = Cat("Felis catus", "Cat", "Carnivore", 4)

my_cat.meow()
print(my_cat)
my_cat.breed("Siamese")

print("********************************************************************************")

class Person: 

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm"
    
person1 = Person("Kholofelo", 22, 173)
print(person1)


class Worker(Person):
    def __init__(self, name, age, height, salary):
        super().__init__(name, age, height) # super() runs the parent’s constructor to set name, age and height
        self.salary = salary # Adds specific attribute

    def calc_yearly_salary(self):
        return self.salary * 12
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm and Salary: {self.salary}" # Override parent method
    
    def __str__(self):
        return super().__str__() + f", Salary: {self.salary}" # If you wanted to reuse the parent __str__() instead of rewriting everything. Extends instead of fully override
        pass

worker1 = Worker("Mace", 25, 180, 10000)
print(worker1)


print("********************************************************************************")

# OPERATOR OVERLOADING

# You can define what happens when you apply any operator on two or more objects 

# Vectors

# A vector is an ordered collection of numbers.
# In mathematics, it represents magnitude (size) and direction.
# In programming (e.g., NumPy), it is often represented as a 1-D array.
# In NumPy it is often written as a vertical array

# For 2-D vectors, we have two values (x, y)
# When we add two vectors, we add two x values and two y values to get a new vector

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other): # Addition of vectors
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other): # Subtraction of vectors
        return Vector(self.x - other.x, self.y - other.y)
        
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"
    
vec1 = Vector(1, 5)
vec2 = Vector(8, 3)

vec3 = vec1 + vec2
vec4 = vec2 - vec3

print(vec3)
print(vec4)