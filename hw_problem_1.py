# HW_P1: City Infrastructure Management System

# Task 1: Vehicle Registration System

'''
Create a Python class Vehicle with attributes registration_number, type, and owner. 
Implement a method update_owner to change the vehicle's owner. Then, create a few 
instances of Vehicle and demonstrate changing the owner.

Expected Outcome: Completion of the Vehicle class with the update_owner method 
and a demonstration script showing the creation of Vehicle objects and updating their owners.
'''

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self):
        new_owner = input("Who is the new owner? ")
        self.owner = new_owner

car1 = Vehicle(1010, "car", "Anthony")
car2 = Vehicle(1011, "suv", "Rosa")
car3 = Vehicle(1012, "truck", "Jose")
car4 = Vehicle(1013, "antique", "Rachel")

print("Vehicle Owners:")
print("Vehicle 1 Owner:", car1.owner)
print("Vehicle 2 Owner:", car2.owner)
print("Vehicle 3 Owner:", car3.owner)
print("Vehicle 4 Owner:", car4.owner)

car3.update_owner()
car4.update_owner()
print("Updated Vehicle Owners:")
print("Vehicle 3 Owner:", car3.owner)
print("Vehicle 4 Owner:", car4.owner)


# Task 2: Event Management System Enhancement
'''
Extend an existing Event class by adding a feature to keep track of the number of participants. Implement 
a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
'''

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    
    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        print(f"Event '{self.name}' has {self.participant_count} participants.")

babyshower = Event("Baby Shower", "April 1")

babyshower.add_participant()
babyshower.add_participant()
babyshower.add_participant()
babyshower.add_participant()
babyshower.add_participant()
babyshower.get_participant_count()
