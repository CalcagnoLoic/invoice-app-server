import sys
from pydantic import BaseModel
from typing import List

from client_address import ClientAddress
from items import Items
from sender_address import SenderAddress


class InvoiceBase(BaseModel):
    id: str
    created_at: str
    payement_due: str
    description: str
    payement_terms: str
    client_name: str
    client_email: str
    status: str
    total: str


class InvoiceCreate(InvoiceBase):
    pass


class Invoice(InvoiceBase):
    sender_address: List[SenderAddress] = []
    client_address: List[ClientAddress] = []
    items: List[Items] = []

    class Config:
        from_attributes = True
