import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

Base = sqlalchemy.orm.declarative_base()


class Invoice(Base):
    __tablename__ = "invoice"

    id = Column(String(6), primary_key=True, autoincrement=False)
    sender_id = Column(
        Integer, ForeignKey("sender_address.id_sender", ondelete="CASCADE")
    )
    client_id = Column(
        String(128), ForeignKey("client_address.client_street", ondelete="CASCADE")
    )
    created_at = Column(String(128))
    payment_due = Column(String(128))
    description = Column(String(128))
    payment_terms = Column(Integer)
    client_name = Column(String(128))
    client_email = Column(String(128))
    status = Column(String(128))
    total = Column(Float)

    sender_address = relationship(
        "SenderAddress", back_populates="invoices", cascade="all", single_parent=True
    )
    client_address = relationship(
        "ClientAddress", back_populates="invoices", cascade="all", single_parent=True
    )
    items = relationship(
        "Items", back_populates="invoice", cascade="all", single_parent=True
    )


class SenderAddress(Base):
    __tablename__ = "sender_address"

    id_sender = Column(Integer, primary_key=True)
    street = Column(String(128))
    invoice_id = Column(String(128))
    city = Column(String(128))
    postCode = Column(String(128))
    country = Column(String(128))

    invoices = relationship("Invoice", back_populates="sender_address")


class ClientAddress(Base):
    __tablename__ = "client_address"

    client_street = Column(String(128), primary_key=True)
    invoice_id = Column(String(128))
    client_city = Column(String(128))
    client_postCode = Column(String(128))
    client_country = Column(String(128))

    invoices = relationship("Invoice", back_populates="client_address")


class Items(Base):
    __tablename__ = "items"

    items_id = Column(Integer, autoincrement=True, primary_key=True)
    invoice_id = Column(String(128), ForeignKey("invoice.id", ondelete="CASCADE"))
    name = Column(String(128))
    quantity = Column(Integer)
    price = Column(Float)
    total = Column(Float)

    invoice = relationship("Invoice", back_populates="items")
