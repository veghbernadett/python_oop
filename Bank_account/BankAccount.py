from abc import ABC, abstractmethod
import random

__author__ = "Bernadett Vegh"

class Customer:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    @property
    def get_name(self):
        return f"{self.name}"
    
    @property
    def get_email(self):
        return f"{self.email}"
    
    @property
    def get_phone_number(self):
        return f"{self.phone_number}"

    def __str__(self) -> str:
        return f"Customer Information: {self.name}, {self.email}, {self.phone_number}"

class BankAccount(ABC):

    @property
    @abstractmethod
    def balance(self):
        pass

    @balance.setter
    @abstractmethod
    def balance(self, value):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod 
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class CheckingAccount(BankAccount):

    _used_account_numbers = set()

    def __init__(self, customer, account_holder=str, initial_balance=0.0):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of the Customer class.")
        
        self.customer = customer
        self.account_holder = account_holder
        self._balance = initial_balance
        self.account_number = self.generate_account_number()

    @staticmethod
    def generate_account_number():
        while True:

            part1 = ''.join(str(random.randint(0, 9)) for n in range(8))
            part2 = ''.join(str(random.randint(0, 9)) for n in range(8))
            part3 = ''.join(str(random.randint(0, 9)) for n in range(8))
            account_number = f"{part1}-{part2}-{part3}"

            if account_number not in CheckingAccount._used_account_numbers:
                CheckingAccount._used_account_numbers.add(account_number)
                return account_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
    
    def deposit(self, amount=float):
        try:
            if amount > 0:
                self.balance += amount
            else:
                raise "Invalid deposit. Add amount more than 0."
        except TypeError:
            raise "Amount should be a positive number."

    def withdraw(self, amount=float):
        try:
            if 0 < amount <= self.balance:
                self.balance -= amount
            else:
                raise "Invalid. The amount should be more than 0 and less than the balance."
        except TypeError:
            raise "Amount should be a positive number."

    def check_balance(self):
        return f"Account balance for {self.account_holder} Account no. {self.account_number}: {self.balance}"
    
    def account_holder_info(self):
        return f"Account info for {self.account_holder}: {self.customer.__str__()}"

class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of the Customer class.")
        self.customers.append(customer)

    def create_account(self, customer, initial_balance=0.0):
        if customer not in self.customers:
            raise ValueError("Customer not found in the bank.")
        account_holder = f"{customer.name[:3].upper()}"
        account = CheckingAccount(customer, account_holder, initial_balance)
        return account
    
    def print_customers(self):
        print("Customers in the bank:")
        for customer in self.customers:
            print(customer.__str__())

def main():
    bank = Bank()

    print("Add first customer")
    my_customer1 = Customer('Test Jane', 'testjane@test.com', '123-4567')
    bank.add_customer(my_customer1)
    my_account1 = bank.create_account(my_customer1, initial_balance=100.0)
    my_account1.deposit(10.6)
    my_account1.withdraw(1.08)
    print(my_account1.check_balance())
    print(my_account1.account_holder_info())
    print("############################################################")

    print("Add second customer")
    my_customer2 = Customer('Happy Tom', 'happytom@test.com', '987-6543')
    bank.add_customer(my_customer2)
    my_account2 = bank.create_account(my_customer2)
    my_account2.deposit(15.0)
    my_account2.withdraw(3.6)
    print(my_account2.check_balance())
    print(my_account2.account_holder_info())
    print("############################################################")

    print("Add third customer")
    customer_name = input("Enter the customer's name: ") # "Unit Test John"
    customer_email = input("Enter the customer's email: ") # "john@test.com"
    customer_phone_no = input("Enter the customer's phone number: ") # "567-1234"
    account_initial_balance = float(input("Enter initial balance: ")) # 1000.0
    account_deposit = float(input("Enter deposit amount: ")) # 500.0
    account_withdraw = float(input("Enter withdraw amount: ")) # 200.0
    
    my_customer3 = Customer(customer_name, customer_email, customer_phone_no)
    bank.add_customer(my_customer3)
    my_account3 = bank.create_account(my_customer3, initial_balance=account_initial_balance)
    my_account3.deposit(account_deposit)
    my_account3.withdraw(account_withdraw)
    print(my_account3.check_balance())  
    print(my_account3.account_holder_info())  
    print("############################################################")

    print("Bank Customer information")
    bank.print_customers()

if __name__ == "__main__":
    main()