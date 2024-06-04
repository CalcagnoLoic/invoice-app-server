from typing import List
from sqlalchemy.orm import Session, joinedload
import models.models as models


def read_all_invoices(db: Session):
    """
    Request to fetch all data invoices
    """
    invoices = (
        db.query(models.Invoice)
        .options(
            joinedload(models.Invoice.sender_address),
            joinedload(models.Invoice.client_address),
            joinedload(models.Invoice.items),
        )
        .order_by(models.Invoice.created_at.desc())
        .all()
    )
    return invoices


def read_invoice_by_id(db: Session, invoice_id: str):
    """
    Request to fetch only one invoice depending on his ID
    """
    invoice = (
        db.query(models.Invoice)
        .options(
            joinedload(models.Invoice.sender_address),
            joinedload(models.Invoice.client_address),
            joinedload(models.Invoice.items),
        )
        .where(models.Invoice.id == invoice_id)
        .first()
    )
    return [invoice]


def create_invoice(db: Session):
    new_invoice = models.Invoice()


"""Réponse Formik
SENDER
id_sender: ??
street: "test"
invoice_id: generator_invoice_id()
city: "test"
postCode: "test"
country: "test"

CLIENT
client_street: "test"
invoice_id: generator_invoice_id()
client_city: "test"
client_postCode: "tes"
client_country: "test"

INVOICE
id: generator_invoice_id()
sender_id=??
client_id=client_street
created_at:"2024-06-05"
payment_due: calculate_due_date()
description: "test"
payment_terms: "14"
client_name: "test"
client_email: "test@gmail.com"
status: "pending"
total: "25"

ITEMS
items: Array(1)
    0: {name: 'test', quantity: '5', price: '5'}
    length: 1
    [[Prototype]]: Array(0)
"""


def delete_one_invoice(db: Session, invoice_id: str):
    invoice_deleted = (
        db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    )
    print({"message": f"Invoice with tag {invoice_id} has been removed!"})
    return invoice_deleted
