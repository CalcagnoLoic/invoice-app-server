from typing import List
from pydantic import BaseModel


class clientAddressBase(BaseModel):
    street: str
    invoice_id: str
    city: str
    post_code: str
    country: str


class ClientAddressCreate(clientAddressBase):
    pass


class ClientAddress(clientAddressBase):
    class Config:
        from_attributes = True


class ItemsBase(BaseModel):
    items_id: int
    invoice_id: str
    name: str
    quantity: int
    price: float
    total: float


class ItemsCreate(ItemsBase):
    pass


class Items(ItemsBase):
    class Config:
        from_attributes = True


class SenderAddressBase(BaseModel):
    id_sender: int
    street: str
    invoice_id: str
    city: str
    post_code: str
    country: str


class SenderAddressCreate(SenderAddressBase):
    pass


class SenderAddress(SenderAddressBase):
    class Config:
        from_attributes = True


class InvoiceBase(BaseModel):
    id: str
    sender_id: int
    client_id: str
    created_at: str
    payment_due: str
    description: str
    payment_terms: str
    client_name: str
    client_email: str
    status: str
    total: float


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase):
    sender_address: List[SenderAddress] = []
    client_address: List[ClientAddress] = []
    items: List[Items] = []

    class Config:
        from_attributes = True
