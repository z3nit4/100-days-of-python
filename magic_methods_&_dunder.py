# Dunder means Double Underscore __

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X is {self.x}, Y: is {self.y}"
    
    def __len__(self):
        return 10
    
    def __call__(self):
        print("Hello I was called.")

v1 = Vector(20,80)
v2 = Vector(60, 30)
v3 = v1 + v2

print(v3)

print(len(v3))

v3() # Call object