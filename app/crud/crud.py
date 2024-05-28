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
        .order_by(models.Invoice.sender_id)
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