from typing import List
from fastapi import FastAPI, Depends, HTTPException
from database.db import engine, SessionLocal
from models.models import Base
from crud.crud import read_all_invoices, read_invoice_by_id
from sqlalchemy.orm import Session
from schemas.schemas import Invoice

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/invoices/", status_code=200)
async def get_all_invoice(db: Session = Depends(get_db)):
    invoices = read_all_invoices(db)
    return invoices


@app.get("/invoices/{invoice_id}", status_code=200)
async def get_invoice(invoice_id: str, db: Session = Depends(get_db)):
    invoice = read_invoice_by_id(db, invoice_id)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice


@app.post("/create-new-invoice/", status_code=201)
async def create_new_invoice(db: Session = Depends(get_db)):
    pass
