from sqlalchemy.orm import Session, joinedload
import models.models as models


def get_invoices(db: Session):
    invoices = (
        db.query(models.Invoice)
        .options(
            joinedload(models.Invoice.sender_address),
            joinedload(models.Invoice.client_address),
            joinedload(models.Invoice.items)
        )
        .all()
    )
    return invoices
