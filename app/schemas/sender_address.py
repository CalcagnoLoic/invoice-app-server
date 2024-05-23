from pydantic import BaseModel


class SenderAddressBase(BaseModel):
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
