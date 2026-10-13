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
        self.employees = []

    def add_employee(self,name, phone, email, address, designation, age, salary ):
        employee = Employee(name, phone, email, address, designation, age, salary)
        self.employees.append(employee)
        print(f"{self.name} added successfully!")

    def view_employee(self):
        print("List of Employees!!")
        for emp in self.employees:
            print(emp.name, emp.designation, emp.phone, emp.email, emp.age, emp.address, emp.salary)
