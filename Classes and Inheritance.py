# Programmer: Zailyn Tamayo; Class: CIS 247; File: Lab13_5.py; Date: 05/31/2013

class FirstClass:                # Define a class object. 
     def setdata(self, value):    # Define class methods. 
         self.data = value        # self is the instance. 
     def display(self): 
         print(self.data)          # self.data: per instance 
 
x = FirstClass()    # Make two instances. 
y = FirstClass()    # Each is a new namespace. 
 
x.setdata("\nCIS 247")  # Call methods: self is x 
y.setdata(3.14159)    # Runs: FirstClass.setdata(y, 3.14159) 
 
x.display()            # self.data differs in each. 
y.display() 
 
class SecondClass(FirstClass):    # Inherits setdata 
     def display(self):       # Changes display  
         print('Current value = "%s"' % self.data) 
 
z = SecondClass() 
z.setdata(42)             # setdata found in FirstClass 
z.display()             # finds overridden method in SecondClass. 
x.display()       # x is still a FirstClass instance (old message). 
 
class ThirdClass(SecondClass):                    # is-a SecondClass 
     def __init__(self, value):                # On "ThirdClass(value)" 
         self.data = value 
     def __add__(self, other):                 # On "self + other" 
         return ThirdClass(self.data + other) 
     def __mul__(self, other): 
         self.data = self.data * other          # On "self * other"  
 
a = ThirdClass("CIS")       # New __init__ called 
a.display(  )               # Inherited method 
 
b = a + '247'             # New __add__: makes a new instance 
b.display() 
 
a * 3                     # New __mul__: changes instance in-place 

a.display()