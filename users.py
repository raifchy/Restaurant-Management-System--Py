from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Employee(User):
    def __init__(self, name, phone, email, address, designation, age, salary):
        super().__init__(name, phone, email, address)
        self.designation = designation
        self.age = age
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()


class Restaurant:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    def view_employee(self):
        print("List of Employees!!")
        for emp in self.employees:
            print(emp.name, emp.designation, emp.phone, emp.email)

