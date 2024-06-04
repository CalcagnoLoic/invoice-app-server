import unittest
from utils.calculate_due_date import *


class TestCalculatorDueDate(unittest.TestCase):
    def test_due_date(self):
        self.assertEqual(calculate_due_date("2024-06-01", 1), "2024-06-02")
        self.assertEqual(calculate_due_date("2024-06-01", 7), "2024-06-08")
        self.assertEqual(calculate_due_date("2024-06-01", 14), "2024-06-15")
        self.assertEqual(calculate_due_date("2024-06-01", 30), "2024-07-01")

