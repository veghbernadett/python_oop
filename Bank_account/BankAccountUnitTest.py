import unittest
from BankAccount import Customer
from BankAccount import CheckingAccount

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

if __name__ == "__main__":
    unittest.main()
