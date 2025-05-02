# # defining class
# class Smartphone:
#     #constructor
#     def __init__(self, device, brand):
#         self.device = device
#         self.brand = brand

#     # Method of the class
#     def description(self):
#         return f"{self.device} of {self.brand} supports Android 14"
    
#     # creating objects of the class
# phoneObj = Smartphone("Smartphone", "Samsung")
# print(phoneObj.description())

# class class_name:
#     x = 'Data Engineering'
# course = class_name()
# print(course.x)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     # def __str__(self):
#     #     return f"{self.name}, {self.age}"
#     def my_function(self):
#         print('My name is ' + self.name)
# p = person('Bright', 12)
# p.my_function()


# defining class
# class Ebook:
#     #constructor
#     def __init__(self, Title, Author, Pages):
#         self.Title = Title
#         self.Author = Author
#         self.Pages = Pages
        

#     # Method of the class
#     def is_long(self):
#         return self.Pages > 300 

#     # creating objects of the class
# E_book = Ebook("Data Engineering", "Ogbonna C. Bright", 2000)
# print(E_book.is_long())


# # defining class
# class Car:
#     #constructor
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
        

#     # Method of the class
#     def display_infor(self):
#         return f"{self.make} {self.model} {self.year}"
    
#     # creating objects of the class
# CarObj = Car("Toyota", "Corolla", "2004")
# print(CarObj.display_infor())

# class my_fullname: #defining class
#     def __init__(self, first_name, middle_name, last_name): #constructor
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name


# class Employee:
#     'Common base class fo all employees'
#     empCount = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
    
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)

#     def displayEmployee(self):
#         print("Name : ", self.name, ", Salary: ", self.salary)
        
# print(Employee.empCount)

# emp1 = Employee('Zara', 5000)
# emp2 = Employee('Bright', 59000)
# emp3 = Employee('Ogbonna', 3000)
# emp1.displayCount()
# emp2.displayCount()
# emp3.displayCount()
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp3.displayEmployee()

# x = 179
# y = 'String'
# z = 3+3j

# class Employee:
#     # class attribute
#     empCount = 0
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#         # Modifying class attribute
#         Employee.empCount+= 1
#         print ("Name:", self._name, ", Age: ", self._age)
#         # accessing class attribute
#         print("Employee Count:", Employee.empCount)

# e1 = Employee("Bhavana", 24)
# print()
# e2 = Employee("Rajesh", 26)

# class Employee:
#     def __init__(self, name="Bhavana", age =24):
#         self.name = name
#         self.age = age
#     def displayEmployee(self):
#         print ("Name:", self.name, ", Age: ", self.age)

# print 


# class student: 
#     def __init__(self, name):
#         self.name = name
#         self.subjects = {}
    
#     def add_subject(self, subject_name):
#         self.subjects[subject_name] = []

#     def add_grade(self, subject_name, grade):
#         if subject_name in self.subjects:
#             self.subjects[subject_name].append(grade)
#         else:
#             print(f"subject '{subject_name}' not found. please add it first.")

#     def calculate_average(self, subject_name):
#         if subject_name in self.subjects and self.subjects[subject_name]:
#            grades = self.subjects[subject_name]
#            return sum(grades) / len(grades)
#         else:
#             return 0.0
# Student = student("Alice")
# Student.add_subject("Maths")
# Student.add_grade("Math", 90)
# Student.add_grade("Math", 85)
# Student.add_grade("Maths", 95)
# Student.add_subject("Science")
# Student.add_grade("Science", 80)
# Student.add_grade("Science", 70)

# print(Student.calculate_average("Math"))
# print(Student.calculate_average("Science"))
# print(Student.subjects)

# class Student:
#     school = "Learn Factory" #Class variable

#     def __init__(self, name): # Instance attr constructor
#         self.name = name # Instance variable

#     def get_stud_name(self): # Instance Method
#         print(self.name)

#     @classmethod            #Decorator
#     def get_school_name(cls):       #Class method
#         print(cls.school)

# s1 = Student("Emeka")
# s2 = Student("John")

# s1.get_stud_name()
# s2.get_stud_name()
# s1.get_school_name()
# s2.get_school_name()


# class Student:
#     school = "Learn Factory" #Class variable
#     cohort = "Cohort 5"

#     def __init__(self, name, age): # Instance attr constructor
#         self.name = name # Instance variable
#         self.age = age
#         self.track = "Data Engineering"

#     def get_instance_attr(self): # Instance Method
#         print(self.name, self.age, self.track )

#     @classmethod            #Decorator
#     def get_class_attr(cls):       #Class method
#         print(cls.school, cls.cohort)

# s1 = Student("Emeka", 30)
# s2 = Student("John", 98)
# s3 = Student("Okorie", 67)
# s4 = Student("Adanna", 76)
# s1.track = "UI/UX"

# s1.get_class_attr()
# s2.get_class_attr()
# s3.get_class_attr()
# s4.get_class_attr()

# s1.get_instance_attr()
# s2.get_instance_attr()
# s3.get_instance_attr()
# s4.get_instance_attr()


#1. person class
# class Person:
#      def __init__(self, name, age):
#          self.name = name
#          self.age = age
# def introduce(self):
#         print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

# #2. Employee class
# class Employee:
#      def __init__(self, company, salary):
#           self.company = company
#           self.salary = salary

# def work(self):
#      print(f"I work at {self.company} and earn $ {self.salary} per year.")

# #3. Manager class inheriting from both Person and Employee
# class Manager(Person, Employee):
#      def __init__(self, name, age, company, salary):
#         # Initialize both parent classes
#         Person.__init__(self, name, age)
#         Employee.__init__(self, company, salary)
    
# def manager(self):
#      print(f"{self.name} is managing the team at {self.company}.")

# #Demonstration 
# manager = Manager("Ogbonna Chimezie Bright", 21, "TechCorp", 50)
# #Accessing methods and attributes from both parents classes
# manager.introduce() #from Person
# manager.work() #from employee
# manager.manage() #specific to Manger

# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
        
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 = Student(m1, m2)
#         return s3
#     def __gt__ (self, other):
#         m1 = self.m1 + self.m1
#         m2 = self.m2 + self.m2
#         if m1 > m2:
#             return True
#         else:
#             return False
        
# s1 = Student(m1=0, m2=0)
# s2 = Student(m1=0, m2=0)
# s1.m1 = int(input("\nEnter the English score of the first student: "))
# s1.m2 = int(input("\nEnter the Mathematics score of the first student: "))

# s2.m1 = int(input("\nEnter the English score of the second student: "))
# s2.m2 = int(input("\nEnter the Mathematics score of the second student: "))


# s3 = s1 + s2

# print(f"\nThe total mark for English for both students is {s3.m1}")
# print(f"\nThe total mark for Mathematics for both students is {s3.m2}")

# print(f"\nThe first student has a total of {s1.m1 + s1.m2} marks")
# print(f"\nThe second student has a total of {s2.m1+s2.m2} marks")
# if s1 > s2:
#     print("\nThe first student wins the contest...")
# else:
#     print("\nThe second student wins the contest...")

# # print(s1.m1)

# class Circle:
#     def area(self, radius):
#         print(f"Area of a circle with radius {radius} is", 3.14 * radius**2)


# class Square:
#     def area(self, length):
#         print(f"The area of square with length {length} is", length**2)


# class Rect: 
#     def area (self, length):
#         print(f"The area of Rect with length {length} is", length**2)

# def calc(shape, size):
#     return shape.area(size)

# sq = Square()
# cir = Circle()
# rect = Rect()

# print(calc(sq, 10))  
# print(calc(cir, 25))
# print(calc(rect, 15))


# class VEctor:
#     def __init__(self, x, y):                    
#         self.x = x
#         self.y = y

#     def __add__(self, other): 
#         return VEctor(self.x-other.x, self.y+other.y)
    
#     def __sub__(self, other):
#         return VEctor(self.x-other.x, self.y+other.y)
    
#     def __str__(self):
#         return f"VEcotor({self.x}, {self.y})"


# v1 = VEctor(1, 3)
# v2  = VEctor(3, 4)
# print(v1 + v2)
# print(v1 - v2)



# class Shape:
#     def area(self, length):
#         print(f"This Method prints the area of a specific shape with dimensinos {length}")
              
# class Circle(Shape):
#     def area(self, radius):
#         super().area(radius)
#         print(f"Area of a circle with radius {radius} is", 3.14 * radius**2)


# class Square(Shape): 
#     def area (self, length):
#         super().area(length)
#         print(f"The area of square with length {length} is", length**2)

# cir = Shape()
# cir.area(10)

# new_cir = Circle()
# new_cir.area(10) 


# import turtle
# import random

# # Triangle drawing class
# class TriangleDrawer:
#     def __init__(self,turtle_obj):
#         self.t = turtle_obj

#     def draw_triangle(self,x,y,size,color):
#         self.t.penup()
#         self.t.goto(x,y)
#         self.t.pendown()
#         self.t.fillcolor(color)
#         self.t.begin_fill()
#         for _ in range(3):
#             self.t.forward(size)
#             self.t.left(120)
#         self.t.end_fill()

# # Random color generator
# def random_color():
#     return(random.random(), random.random(), random.random())

# # Set up screen
# screen = turtle.Screen()
# screen.colormode(1.0) # Use RGB values between 0 and 1
# screen.bgcolor(random_color()) # Random background color

# # Create turtle object
# t =turtle.Turtle()
# t.speed(3)
# drawer = TriangleDrawer(t)

# # Draw 4 triangles in a column
# start_x = -50
# start_y = 100
# triangle_size = 100
# gap = 120

# for i in range(4):
#     color = random_color()
#     drawer.draw_triangle(start_x, start_y-i*gap, triangle_size, color)

# turtle.done()

# import turtle
# import random

# #  Base Shape class:
# class Shape:
#     def __init__(self, turtle_obj, color, x, y):
#         self.t = turtle_obj
#         self.color = color
#         self.x = x
#         self.y = y

#     def draw(self):
#         pass

#     def setup(self):
#         self.t.penup()
#         self.t.goto(self.x, self.y)
#         self.t.pendown()
#         self.t.fillcolor(self.color)
#         self.t.begin_fill()
    
#     def finish(self):
#         self.t.end_fill()

# # Shape subclasses
# class Square(Shape):
#     def draw(self):
#         for _ in range(4):
#             self.t.forward(50)
#             self.t.right(90)
#         self.finish()
    

# class Rectangle(Shape):
#     def draw(self):
#         self.setup()
#         for _ in range(2):
#             self.t.forward(80)
#             self.t.right(90)
#             self.t.forward(40)
#             self.t.right(90)
#         self.finish()


# class Triangle(Shape):
#     def draw(self):
#         for _ in range(3):
#             self.t.forward(60)
#             self.t.left(120)
#         self.finish()

# class Hexagon(Shape):
#     def draw(self):
#         for _ in range(6):
#             self.t.forward(40)
#             self.t.right(60)
#         self.finish()

# class Octagon(Shape):
#     def draw(self):
#         for _ in range(8):
#             self.t.forward(40)
#             self.t.right(45)
#         self.finish()

# # Random color generator
# def random_color():
#     return(random.random(), random.random(), random.random())


# # Random position generator within screen bounds
# def random_position():
#     return(random.randint(-200, 200), random.randint(-200, 200))

# # Setup screen
# screen = turtle.Screen()
# screen.colormode(1.0)
# screen.bgcolor(random_color())

# # Turtle setup?t = 


# class School:
#     def __init__(self, School_name):
#         self.School_name = School_name
        
#     def add_student(self, name, age, grade):
#         new_school = self.school(name, age, grade)
#         self.School_name.append(new_school)
 
#     def list_student(self):
#         print(f"Students" in "{self.School_name}:")
#         for student in self.school:
#             print(student.get_info())

#     # Inner class
#     class Student:
#         def __init__(self, name, age, grade):
#             self.name = name
#             self.age = age
#             self.grade = grade

#         def get_info(self):
#             return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
        
# # Usage
# student = School("Learn Factory")
# student.add_student("2020", "Accounting", 100)
# student.add_student("Bright", 21, "1st position" )

# student.list_student()


def getA(self):
    return self.a


anon_class = type("", (object,), {"a": 5, "b": 6, "c:": 7, "getA": getA, "getB": lambda self: self.b})
obj = anon_class()
print(obj.getA(), obj.getB())