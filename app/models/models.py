import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(String(6), primary_key=True, autoincrement=False)
    sender_id = Column(String(128), ForeignKey("sender_address.street"))
    client_id = Column(String(128), ForeignKey("client_address.street"))
    created_at = Column(String(128), name="createdAt")
    payment_due = Column(String(128), name="paymentDue")
    description = Column(String(128))
    payment_terms = Column(String(128), name="paymentTerms")
    client_name = Column(String(128), name="clientName")
    client_email = Column(String(128), name="clientEmail")
    status = Column(String(128))
    total = Column(Integer)

    sender_address = relationship("SenderAddress", back_populates="invoices")
    client_address = relationship("ClientAddress", back_populates="invoices")
    items = relationship("Items", back_populates="invoice")


class SenderAddress(Base):
    __tablename__ = "sender_address"

    street = Column(String(128), primary_key=True)
    invoice_id = Column(String(128))
    city = Column(String(128))
    post_code = Column(String(128), name="postCode")
    country = Column(String(128))

    invoices = relationship("Invoice", back_populates="sender_address")


class ClientAddress(Base):
    __tablename__ = "client_address"

    street = Column(String(128), primary_key=True)
    invoice_id = Column(String(128))
    city = Column(String(128))
    post_code = Column(String(128), name="postCode")
    country = Column(String(128))

    invoices = relationship("Invoice", back_populates="client_address")


class Items(Base):
    __tablename__ = "items"

    items_id = Column(Integer, autoincrement=True, primary_key=True)
    invoice_id = Column(String(128), ForeignKey("invoice.id"))
    name = Column(String(128))
    quantity = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)

    invoice = relationship("Invoice", back_populates="items")
