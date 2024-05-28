from pydantic import BaseModel
from typing import List, Optional


class SenderAddress(BaseModel):
    id_sender: int
    street: str
    invoice_id: str
    city: str
    postCode: str
    country: str


class ClientAddress(BaseModel):
    client_street: str
    invoice_id: str
    client_city: str
    client_postCode: str
    client_country: str


class Item(BaseModel):
    items_id: int
    invoice_id: str
    name: str
    quantity: int
    price: float
    total: float


class InvoiceBase(BaseModel):
    id: str
    sender_id: int
    client_id: str
    created_at: str
    payment_due: str
    description: str
    payment_terms: str
    client_name: str
    client_email: Optional[str]
    status: str
    total: float


class InvoiceCreate(InvoiceBase):
    sender_address: SenderAddress
    client_address: ClientAddress
    items: List[Item]


class Invoice(InvoiceBase):
    sender_address: SenderAddress
    client_address: ClientAddress = None
    items: List[Item]

    class Config:
        from_attributes = True
