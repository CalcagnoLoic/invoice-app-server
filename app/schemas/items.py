from pydantic import BaseModel


class ItemsBase(BaseModel):
    name: str
    quantity: int
    price: int
    total: int


class ItemsCreate(ItemsBase):
    pass


class Items(ItemsBase):
    class Config:
        from_attributes = True
