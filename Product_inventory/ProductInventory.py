"""
Create an application which manages an inventory of products. 
Create a product class which has a price, id, and quantity on hand. 
Then create an inventory class which keeps track of various products 
and can sum up the inventory value.
"""

import random
import string
from abc import ABC, abstractmethod

class Product(ABC):
    _used_ids = set()

    def __init__(self, name=str, price=int, quantity=int):
        self._id = self.generate_id()
        self._name = name
        self._price = price
        self._quantity = quantity

    @staticmethod
    def generate_id():
        while True:

            letters = ''.join(random.choices(string.ascii_uppercase, k=4))
            digits = ''.join(random.choices(string.digits, k=4))

            id = f"{letters}-{digits}"

            if id not in Product._used_ids:
                Product._used_ids.add(id)
                return id

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    @property
    def quantity(self):
        return self._quantity
    
    @property
    @abstractmethod
    def calculate_value(self):
        pass
    
    @property
    @abstractmethod
    def product_info(self):
        pass

class ConcreteProduct(Product):

    def calculate_value(self):
        return self.price * self.quantity
    
    def product_info(self) -> list:
        return [self.id, self.name, self.price, self.quantity, self.calculate_value()]

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total: {self.calculate_value()}"
    

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, ConcreteProduct):
            raise ValueError("Product must be an instance of the Product class.")
        self.products.append(product)

    def delete_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                return
        raise f"Product with ID {id} not found in inventory."

    def print_products(self):
        print("Products in Inventory:")
        for product in self.products:
            print(product.__str__())

    def inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.product_info()[-1]
        return total_value

def main():
    product1 = ConcreteProduct("Laptop", 1200, 5)
    product2 = ConcreteProduct("Monitor", 300, 3)
    print("First and second product are added automatically.")
    print("Please add third product!")
    product3_name = input("Enter the product's name: ") #"Keyboard"
    product3_price = int(input("Enter the product's price: ")) #1000
    product3_qt = int(input("Enter the product's quantity: ")) #2
    product3 = ConcreteProduct(product3_name, product3_price, product3_qt)

    inventory = Inventory()
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)
    print(inventory.print_products())
    print(f"Total value of inventory: {inventory.inventory_value()}")
    # delete product
    inventory.delete_product(product2.id)
    print("Inventory after deletion")
    print(inventory.print_products())
    print(f"Total value of inventory: {inventory.inventory_value()}")

if __name__ == "__main__":
    main()