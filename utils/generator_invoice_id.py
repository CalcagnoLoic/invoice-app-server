import string
import random


def generator_invoice_id() -> string:
    """Generate a new ID for each invoices.

    Returns:
        The ID of each invoice in XX0000 format.
    """

    letter = string.ascii_uppercase
    number = string.digits

    letters = "".join([str(random.choices(letter)) for _ in range(2)])
    numbers = "".join(str(random.choices(number)) for _ in range(4))

    print("{}{}".format(letters, numbers))
    return "{}{}".format(letters, numbers)

generator_invoice_id()