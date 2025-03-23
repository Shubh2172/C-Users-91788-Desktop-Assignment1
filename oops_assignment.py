
Q1. Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle.

class vehicle:
    def __init__(self,name_of_vehicle, max_speed,average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle=average_of_vehicle
    def return_details()
Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class. Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.

class car(vehicle):
    def __init__(self,seating_capacity):
        self.seating_capacity=seating_capacity
    def return_details(self):
         return self.name_of_vehicle , self.seating_capacity
thar=vehicle('mahindra',120,12)
thar=car(4)
Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

class noida:
    def metropolitan(self):
        print("ha hai")
class mera_gaav:
    def hariyali(self):
        print("ha hai")
class gkp(noida , mera_gaav):
    #in these class properties of above two classes will work
    pass
Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this class.

class love:
    def __init__(self,romance,friedship):
        self.__romance= romance
        self.friendship=friendship
    @property
    def romance_exposed(self):
        return self.__romance
    @romance_exposed.setter
    def romance_changed(self,prem):
        self.__romance=prem
        
Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

import abc
class details:
    @abc.abstractmethod
    def name(self):
        pass
    @abc.abstractmethod
    def roll_no(self):
        pass
    
class ram(details):
    def name(self):
        return 'ram'
    def roll_no(self):
        return 26
    
student26=ram()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[12], line 1
----> 1 student26=ram()

NameError: name 'ram' is not defined
student26.name
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[11], line 1
----> 1 student26.name

NameError: name 'student26' is not defined
 