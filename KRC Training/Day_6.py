######################################################
## Internship @ KRC: DAY 6                          ##
## ANIMIKH AICH                                     ##
## RNS Institute of Technology, Bengaluru, India    ##
######################################################

# OOPs Concepts

class myClass:
    '''This is a documentation String for the class
This can be accessed by usning myClass.__doc__'''
    pass

class Employee:
    '''This is the documentation for a base class defining all employees'''
    __empCount = 0                      #Declaring as private class variable
    empCount = __empCount

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__empCount += 1
        Employee.empCount = Employee.__empCount


    def dispCount(self):
        print('Total Employee {}'.format(Employee.__empCount))

    def displayEmployee(self):
        print('Name:', self.name,'\t', 'Salary:', self.salary)




print('Documentation of the First class',myClass.__doc__)
print('Documentation of the Second class',Employee.__doc__)

manager_1 = Employee('Arun', 150000)
print('After creating 1 object, the count is: ', Employee.empCount)
manager_2 = Employee('Hitesh', 100000)
print('After creating 2 objects, the count is: ', Employee.empCount)
engineer_1 = Employee('Animikh', 90000)
print('After creating 3 objects, the count is: ', Employee.empCount)

print('Documentation can also be invoked using object and dot operator: ',manager_1.__doc__)

manager_1.displayEmployee()
manager_2.displayEmployee()
engineer_1.displayEmployee()

print('Explicitly setting the salary post object creation: ')
manager_1.salary = 100000
print('Updated salary for manager_1: ', manager_1.salary)
manager_1.displayEmployee()

print('Class Name: ', Employee.__name__)
print('Class Documentation: ', Employee.__doc__)
print('Class Module: ', Employee.__module__)
print('Class Bases: ', Employee.__bases__)
print('Class Dictionary: ', Employee.__dict__)

# print('First Object Name: ', manager_1.__name__)          ---- Doesn't Work
print('First Object Documentation: ', manager_1.__doc__)
print('First Object Module: ', manager_1.__module__)
# print('First Object Bases: ', manager_1.__bases__)        ---- Doesn't Work
print('First Object Dictionary: ', manager_1.__dict__)

print('Creating another Class')

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3))
print('Deleting pt1')
del pt1
print('Deleting pt2')
del pt2
print('Deleting pt3')
del pt3
# Destructor is called after deleting all the objects

print('Class Inheritance')

print('Defining parent class')

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

print('Defining child class')

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
