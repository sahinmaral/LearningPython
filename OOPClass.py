import datetime
import math

class Person:
    address = ''
    def __init__(self,name,birthYear):
        self.name = name
        self.birthYear = birthYear

    def calculateAge(self):
        return datetime.date.today().year - self.birthYear


person1 = Person('sahin',2000)
person1.address = 'Test address'
print(person1.name)
print(person1.birthYear)
print(person1.address)
print(person1.calculateAge())

class Circle:
    pi = math.pi
    area = 0
    curriculum = 0

    def __init__(self,radius):
        self.radius = radius
    
    def calculateArea(self):
        self.area =  self.pi * (self.radius ** 2)
    
    def calculateCurriculum(self):
        self.curriculum = 2 * self.pi * self.radius

circle1 = Circle(radius=3)
circle1.calculateArea()
circle1.calculateCurriculum()
print(circle1.area)
print(circle1.curriculum)