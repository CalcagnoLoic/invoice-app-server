import unittest
import re
from utils.generator_invoice_id import *


class TestGeneratorInvoiceID(unittest.TestCase):
    def test_length_id(self):
        id = generator_invoice_id()
        self.assertEqual(len(id), 6)

    def test_pattern_id(self):
        string = generator_invoice_id()
        pattern = "\D{2}\d{4}"

        self.assertEqual(re.search(pattern, string), True)
