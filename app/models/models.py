import sys, sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(String, primary_key=True, autoincrement=False)
    created_at = Column(String, name="createdAt")
    payement_due = Column(String, name="paymentDue")
    description = Column(String)
    payment_terms = Column(String, name="paymentTerms")
    client_name = Column(String, name="clientName")
    client_email = Column(String, name="clientEmail")
    status = Column(String)
    total = Column(Integer)

    sender_address = relationship("SenderAddress", back_populates="invoice_sender")
    client_address = relationship("ClientAddress", back_populates="invoice_client")
    items = relationship("Items", back_populates="invoice_items")


class SenderAddress(Base):
    __tablename__ = "sender_address"

    street = Column(String, primary_key=True)
    invoice_id = Column(String, ForeignKey("invoice.id"))
    city = Column(String)
    post_code = Column(String, name="postCode")
    country = Column(String)

    invoice_sender = relationship("Invoice", back_populates="sender_address")


class ClientAddress(Base):
    __tablename__ = "client_address"

    street = Column(String, primary_key=True)
    invoice_id = Column(String, ForeignKey("invoice.id"))
    city = Column(String)
    post_code = Column(String, name="postCode")
    country = Column(String)

    invoice_client = relationship("Invoice", back_populates="client_address")


class Items(Base):
    __tablename__ = "items"

    items_id = Column(Integer, autoincrement=True, primary_key=True)
    invoice_id = Column(String, ForeignKey("invoice.id"))
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Integer)
    total = Column(Integer)

    invoice_items = relationship("Invoice", back_populates="items")
