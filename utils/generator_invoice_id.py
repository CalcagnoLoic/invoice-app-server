import string
import random


def generator_invoice_id() -> string:
    """Generate a new ID for each invoices.

    Returns:
        The ID of each invoice in XX0000 format.
    """

    letter = string.ascii_uppercase
    letters = "".join(random.choices(letter, k=2))

    number = string.digits
    numbers = "".join(random.choices(number, k=4))

    return "{}{}".format(letters, numbers)


generator_invoice_id()
