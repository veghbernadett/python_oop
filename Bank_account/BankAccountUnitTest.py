import unittest
from BankAccount import Customer, CheckingAccount, Bank

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Unit Test John", "john@test.com", "567-1234")

    def test_full_name(self):
        self.assertEqual(self.customer.name, "Unit Test John")

    def test_email(self):
        self.assertEqual(self.customer.email, "john@test.com")

    def test_phone_number(self):
        self.assertEqual(self.customer.phone_number, "567-1234")

    def test_set_email(self):
        self.customer.email = "new_email@example.com"
        self.assertEqual(self.customer.email, "new_email@example.com")

    def test_set_phone_number(self):
        self.customer.phone_number = "555-4321"
        self.assertEqual(self.customer.phone_number, "555-4321")

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        customer = Customer("Unit Test John", "john@test.com", "567-1234")
        self.account = CheckingAccount(customer, "UTJ", initial_balance=1000.0)

    def test_balance(self):
        self.assertEqual(self.account.balance, 1000.0)

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)

    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.balance, 800.0)

    def test_check_balance(self):
        expected_output = (
            f"Account balance for UTJ Account no. {self.account.account_number}: 1000.0"
        )
        self.assertEqual(self.account.check_balance(), expected_output)

    def account_holder_info(self):
        expected_output = (
            "Account info for UTJ: Customer Information: Unit Test John, john@test.com, 567-1234"
        )
        self.assertEqual(self.account.account_holder_info(), expected_output)

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

        self.customer1 = Customer("John Johny", "johny@test.com", "444-1234")
        self.customer2 = Customer("Tom Tommy", "tomy@test.com", "666-8901")

    def test_add_customer(self): 
        self.bank.add_customer(self.customer1)
        self.assertIn(self.customer1, self.bank.customers)

    def test_create_account(self):
        self.bank.add_customer(self.customer2)
        account = self.bank.create_account(self.customer2, initial_balance=1000.0)
        self.assertIsInstance(account, CheckingAccount)

    def test_print_customers(self):
        self.bank.add_customer(self.customer1)
        self.bank.add_customer(self.customer2)

        with self.assertLogs() as log:
            self.bank.print_customers()

            expected_output = [
                f"INFO:root:Customers in the bank:",
                f"INFO:root:Customer Information: John Johny, johny@test.com, 444-1234",
                f"INFO:root:Customer Information: Tom Tommy, tomy@test.com, 666-8901"
            ]
            self.assertEqual(log.output, expected_output)       

if __name__ == "__main__":
    unittest.main()
