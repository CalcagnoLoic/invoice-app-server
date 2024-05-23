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
