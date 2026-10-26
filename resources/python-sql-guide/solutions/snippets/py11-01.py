import unittest
class Account:
    def __init__(self, balance=0): self.balance = balance
    def withdraw(self, amount):
        if amount <= 0: raise ValueError("amount must be positive")
        if amount > self.balance: raise ValueError("insufficient funds")
        self.balance -= amount
        return self.balance
class AccountTests(unittest.TestCase):
    def setUp(self): self.acct = Account(100)                      # fresh fixture for every test
    def test_withdraw_reduces_balance(self):
        self.assertEqual(self.acct.withdraw(30), 70)
    def test_cannot_overdraw(self):
        with self.assertRaisesRegex(ValueError, "insufficient"): self.acct.withdraw(101)
    def test_rejects_non_positive_amounts(self):
        for bad in (0, -5):
            with self.subTest(amount=bad):                          # parametrised cases with separate reporting
                with self.assertRaises(ValueError): self.acct.withdraw(bad)
    def test_exact_balance_can_be_withdrawn(self):
        self.assertEqual(self.acct.withdraw(100), 0)                # boundary value
import io
result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(unittest.defaultTestLoader.loadTestsFromTestCase(AccountTests))
print("ran", result.testsRun, "tests | failures:", len(result.failures), "| errors:", len(result.errors))
