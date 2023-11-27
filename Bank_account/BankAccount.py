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

def main():
    my_customer1 = Customer('Test Jane', 'testjane@test.com', '123-4567')
    my_account1 = CheckingAccount(my_customer1,"TJ", initial_balance=100.0)
    my_account1.deposit(10.6)
    my_account1.withdraw(1.08)
    print(my_customer1.get_name)
    print(my_account1.check_balance())
    print(my_account1.account_holder_info())
    print(my_account1.customer.get_name)
    print(my_account1.balance)

    my_customer2 = Customer('Test Tom', 'testtom@test.com', '987-6543')
    my_account2 = CheckingAccount(my_customer2, "TT")
    my_account2.deposit(15.0)
    my_account2.withdraw(3.6)
    print(my_customer2.get_name)
    print(my_account2.check_balance())  
    print(my_account2.account_holder_info())  
    print(my_account2.customer.get_name)

    customer_name = input("Enter the customer's name: ") # "Unit Test John"
    customer_email = input("Enter the customer's email: ") # "john@test.com"
    customer_phone_no = input("Enter the customer's phone number: ") # "567-1234"
    account_holder_id = input("Enter the account holder id: ") # "UTJ"
    account_initial_balance = float(input("Enter initial balance: ")) # 1000.0
    account_deposit = float(input("Enter deposit amount: ")) # 500.0
    account_withdraw = float(input("Enter withdraw amount: ")) # 200.0

    my_customer3 = Customer(customer_name, customer_email, customer_phone_no)
    my_account3 = CheckingAccount(my_customer3, account_holder_id, initial_balance=account_initial_balance)
    my_account3.deposit(account_deposit)
    my_account3.withdraw(account_withdraw)
    print(my_customer3.get_name)
    print(my_account3.check_balance())  
    print(my_account3.account_holder_info())  
    print(my_account3.customer.get_name)

if __name__ == "__main__":
    main()