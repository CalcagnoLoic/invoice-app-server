from fastapi import FastAPI, Depends
from database.db import engine, SessionLocal
from models.models import Invoice, SenderAddress, ClientAddress, Items, Base
from crud.reading import get_invoices
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/invoice/")
async def get_all_invoice(db: Session = Depends(get_db)):
    invoice = get_invoices(db)
    return invoice
