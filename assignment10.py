Ques-1

class Animal():
        def __init__(self,legs=2,eyes=2):
                self.legs = legs
                self.eyes = eyes
        def animal_attribute(self):
                print(self.legs)
                print(self.eyes)
class Tiger(Animal):
        pass
obj = Tiger()
obj.animal_attribute()

Ques-2

'''
In this ques, a is an object of class A and b is the object of class B. When a.f() is called, then f method will be executed that will jump to g method and it will print A. 
When b.f() is called, then g method of class B will be executed and it will print B.
So, the output will be:
A B
'''

Ques-3

class Cop():
        def __init__(self,name,age,work,experience,designation):
                self.name=name
                self.age=age
                self.work=work
                self.experience=experience
                self.designation=designation
        def add(self):
                input("Enter name: ")
                input("Enter age: ")
                input("Enter work: ")
                input("Enter experience: ")
                input("Enter designation: ")
        def display(self):
                print(self.name)
                print(self.age)
                print(self.work)
                print(self.experience)
                print(self.designation)
        def update(self):
                self.name = 'a'
                self.age = 20
                self.work = 'business'
                self.experience = 'one year'
                self.designation = 'boss'
class Mission(Cop):
        def __init__(self):
                pass
        def add_mission_details(self,name,age,work,experience,designation):
                pass
obj = Cop('d',10,'study','zero','student')
obj.display()
obj.update()
obj.add()

Ques-4

class Shape():
        def __init__(self,length,breadth,side):
                self.length = length
                self.breadth = breadth
                self.side = side
        def Area(self):
                pass
class Rectangle(Shape):
        def Area(self):
                print(self.length * self.breadth)
class Square(Shape):
        def Area(self):
                print(self.side ** 2)
obj1 = Rectangle(2,3,4)
obj1.Area()
obj2 = Square(2,3,4)
obj2.Area()


