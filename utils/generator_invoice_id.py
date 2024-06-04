import string
import random


def generator_invoice_id() -> string:
    """Generate a new ID for each invoices.

    Returns:
        The ID of each invoice in XX0000 format.
    """

    letter = string.ascii_uppercase
    number = string.digits

    letters = "".join(random.choices(letter) for _ in range(2))
    numbers = "".join(random.choices(number) for _ in range(4))

    return "{}{}".format(letters, numbers)
