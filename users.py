from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = []

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
    def add_to_cart(self, restaurant, item_name):
        item = restaurant.menu.find_item(item_name)
        if item:
            self.cart.append(item)
        else:
            print(item_name + "not found")

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[ item ] += quantity
        else:
            self.items[ item ] = quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(item + "not found!")

    def total_price(self):
        return sum( item.price * quantity for item, quantity in self.items.items() )

    def clear(self):
        self.items = {}



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

    def add_menu_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_menu_item(self, restaurant, item):
        restaurant.menu.remove_menu_item(item)

    def show_menu(self, restaurant):
        restaurant.menu.show_menu()


class Restaurant:
    def __init__(self):
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("List of Employees!!")
        for emp in self.employees:
            print(emp.name, emp.designation, emp.phone, emp.email)


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item} deleted")
        else:
            print(f"{item_name} not found")

    def show_menu(self):
        print("-----Menu-----")
        print(f"Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")


class FootItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
